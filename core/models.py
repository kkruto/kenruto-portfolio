# core/models.py

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email


class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('work', 'Work Experience'),
        ('project', 'Project'),
        ('education', 'Education'),
        ('award', 'Award'),
    ]
    
    type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    achievements = models.JSONField(default=list, blank=True)
    tech_stack = models.JSONField(default=list, blank=True)
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.title} at {self.organization}"


class NowItem(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, help_text="Emoji or icon name (e.g., 📚, 🚀, 🎬)")
    description = models.TextField()
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "What I'm Doing Now"
        verbose_name_plural = "What I'm Doing Now Items"
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('product', 'Technical Product Management'),
        ('engineering', 'Engineering & Data'),
        ('leadership', 'Leadership'),
        ('design', 'Design & Creativity'),
    ]
    
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


# ============================================
# NEW: ARTICLE MODEL FOR BLOG/ESSAYS
# ============================================

class Article(models.Model):
    """
    Model for blog posts, essays, and visual/data essays
    Supports rich content with images, embeds, and code
    """
    
    ARTICLE_TYPES = [
        ('essay', 'Essay'),
        ('visual_essay', 'Visual Essay'),
        ('data_essay', 'Data Essay'),
        ('tutorial', 'Tutorial'),
        ('case_study', 'Case Study'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200, help_text="Article title")
    slug = models.SlugField(unique=True, max_length=200, help_text="URL-friendly version of title")
    article_type = models.CharField(max_length=20, choices=ARTICLE_TYPES, default='essay')
    excerpt = models.TextField(max_length=500, help_text="Short description for listing pages")
    
    # Content
    content = models.TextField(help_text="Main article content (supports HTML)")
    
    # Visual Content
    featured_image = models.ImageField(
        upload_to='articles/images/',
        blank=True,
        null=True,
        help_text="Main image shown at top of article"
    )
    image_caption = models.CharField(max_length=200, blank=True)
    
    # Data Essay Specific (for charts, visualizations)
    has_interactive_content = models.BooleanField(
        default=False,
        help_text="Check if article includes charts, graphs, or interactive elements"
    )
    custom_css = models.TextField(
        blank=True,
        help_text="Custom CSS for this article (optional)"
    )
    custom_javascript = models.TextField(
        blank=True,
        help_text="Custom JavaScript for interactive content (optional)"
    )
    
    # Metadata
    tags = models.JSONField(
        default=list,
        blank=True,
        help_text='Tags as list, e.g., ["product", "design", "AI"]'
    )
    read_time = models.IntegerField(
        default=5,
        help_text="Estimated reading time in minutes"
    )
    
    # Publishing
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # SEO
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="SEO meta description (150-160 chars)"
    )
    
    # Featured/Pinned
    is_featured = models.BooleanField(
        default=False,
        help_text="Show in featured section on home page"
    )
    
    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = "Article/Essay"
        verbose_name_plural = "Articles/Essays"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Set published_date when status changes to published
        if self.status == 'published' and not self.published_date:
            self.published_date = timezone.now()
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    @property
    def is_published(self):
        return self.status == 'published'


# ============================================
# NEW: GALLERY MODEL
# ============================================

class GalleryItem(models.Model):
    """
    Model for gallery items - photos, artwork, projects
    """
    
    GALLERY_TYPES = [
        ('photo', 'Photography'),
        ('design', 'Design Work'),
        ('art', 'Art'),
        ('project', 'Project Screenshot'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    thumbnail = models.ImageField(
        upload_to='gallery/thumbnails/',
        blank=True,
        null=True,
        help_text="Optional thumbnail (will use main image if not provided)"
    )
    
    gallery_type = models.CharField(max_length=20, choices=GALLERY_TYPES, default='photo')
    tags = models.JSONField(default=list, blank=True)
    
    # Optional link (e.g., to full project, Behance, etc.)
    external_link = models.URLField(blank=True)
    
    # Ordering and visibility
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"
    
    def __str__(self):
        return self.title


# ============================================
# NEW: RECENT ACTIVITY (for home page)
# ============================================

class RecentActivity(models.Model):
    """
    Model for "Recently" section on home page
    Can be articles, projects, or any activity
    """
    
    ACTIVITY_TYPES = [
        ('article', 'Published Article'),
        ('project', 'Shipped Project'),
        ('talk', 'Gave Talk'),
        ('achievement', 'Achievement'),
        ('learning', 'Learning'),
        ('other', 'Other'),
    ]
    
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, help_text="Link to article, project, etc.")
    date = models.DateField()
    
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date', 'order']
        verbose_name = "Recent Activity"
        verbose_name_plural = "Recent Activities"
    
    def __str__(self):
        return f"{self.get_activity_type_display()}: {self.title}"


# ============================================
# NEW: RESUME/CV MODEL
# ============================================

class Resume(models.Model):
    """
    Model for resume/CV
    Only one resume should be active at a time
    """
    
    title = models.CharField(
        max_length=200,
        default="Ken Ruto - Resume",
        help_text="Title for the resume"
    )
    
    # Resume file
    resume_file = models.FileField(
        upload_to='resume/',
        help_text="Upload PDF resume"
    )
    
    # Online resume content (optional - for HTML version)
    summary = models.TextField(blank=True, help_text="Professional summary")
    
    is_active = models.BooleanField(
        default=True,
        help_text="Set as active resume (only one should be active)"
    )
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Resume/CV"
        verbose_name_plural = "Resumes/CVs"
    
    def __str__(self):
        return f"{self.title} ({'Active' if self.is_active else 'Inactive'})"
    
    def save(self, *args, **kwargs):
        # Ensure only one active resume
        if self.is_active:
            Resume.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text="Mark as read after reviewing")

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.submitted_at.strftime('%Y-%m-%d')}"