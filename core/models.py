from django.db import models
from django.utils import timezone

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
    achievements = models.JSONField(default=list, blank=True)  # List of achievements
    tech_stack = models.JSONField(default=list, blank=True)  # List of technologies
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.title} at {self.organization}"


class NowItem(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, help_text="Emoji or icon name")
    description = models.TextField()
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('product', 'Technical Product Management'),
        ('engineering', 'Engineering & Data'),
        ('leadership', 'Leadership'),
    ]
    
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"