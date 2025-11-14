# core/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    NewsletterSubscriber,
    Experience,
    NowItem,
    Skill,
    Article,
    GalleryItem,
    RecentActivity,
    Resume,
    ContactMessage
)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    date_hierarchy = 'subscribed_at'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'type', 'start_date', 'is_current', 'order']
    list_filter = ['type', 'is_current']
    search_fields = ['title', 'organization', 'description']
    ordering = ['-start_date']
    list_editable = ['order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('type', 'title', 'organization', 'location')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Content', {
            'fields': ('description', 'achievements', 'tech_stack', 'link')
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )


@admin.register(NowItem)
class NowItemAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'order', 'is_active']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'icon', 'description', 'link')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active'),
            'description': 'Control ordering and visibility on home page'
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']
    ordering = ['category', 'order']


# ============================================
# ENHANCED ARTICLE ADMIN FOR VISUAL ESSAYS
# ============================================

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'article_type_badge',
        'status_badge',
        'published_date', 
        'read_time',
        'is_featured',
        'view_count'
    ]
    list_filter = ['status', 'article_type', 'is_featured', 'published_date']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    list_editable = ['is_featured']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'article_type', 'status')
        }),
        ('Content', {
            'fields': ('excerpt', 'content'),
            'description': 'Use HTML for formatting. See guide below for visual essay tips.'
        }),
        ('Visual Content', {
            'fields': ('featured_image', 'image_caption'),
            'classes': ('collapse',),
        }),
        ('Interactive Content (for Data Essays)', {
            'fields': ('has_interactive_content', 'custom_css', 'custom_javascript'),
            'classes': ('collapse',),
            'description': 'Add custom CSS/JS for charts, graphs, or interactive elements'
        }),
        ('Metadata', {
            'fields': ('tags', 'read_time', 'meta_description'),
            'classes': ('collapse',),
        }),
        ('Publishing', {
            'fields': ('published_date', 'is_featured'),
        }),
    )
    
    def article_type_badge(self, obj):
        colors = {
            'essay': '#3b82f6',
            'visual_essay': '#8b5cf6',
            'data_essay': '#10b981',
            'tutorial': '#f59e0b',
            'case_study': '#ef4444',
        }
        color = colors.get(obj.article_type, '#6b7280')
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; '
            'border-radius: 12px; font-size: 11px; font-weight: bold;">{}</span>',
            color,
            obj.get_article_type_display()
        )
    article_type_badge.short_description = 'Type'
    
    def status_badge(self, obj):
        colors = {
            'draft': '#6b7280',
            'published': '#10b981',
            'archived': '#ef4444',
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; '
            'border-radius: 12px; font-size: 11px;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    
    def view_count(self, obj):
        return format_html(
            '<a href="{}" target="_blank">View →</a>',
            obj.get_absolute_url()
        )
    view_count.short_description = 'Actions'
    
    class Media:
        css = {
            'all': ('admin/css/article_admin.css',)
        }
        js = ('admin/js/article_admin.js',)
    
    # Save actions
    actions = ['make_published', 'make_draft', 'make_featured']
    
    def make_published(self, request, queryset):
        updated = queryset.update(status='published')
        self.message_user(request, f'{updated} article(s) published.')
    make_published.short_description = "Publish selected articles"
    
    def make_draft(self, request, queryset):
        updated = queryset.update(status='draft')
        self.message_user(request, f'{updated} article(s) marked as draft.')
    make_draft.short_description = "Mark as draft"
    
    def make_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} article(s) marked as featured.')
    make_featured.short_description = "Mark as featured"


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'title', 'gallery_type', 'order', 'is_visible']
    list_filter = ['gallery_type', 'is_visible']
    list_editable = ['order', 'is_visible']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'gallery_type')
        }),
        ('Images', {
            'fields': ('image', 'thumbnail'),
            'description': 'Upload main image (thumbnail is optional)'
        }),
        ('Additional Info', {
            'fields': ('tags', 'external_link'),
            'classes': ('collapse',),
        }),
        ('Display', {
            'fields': ('order', 'is_visible'),
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; '
                'object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No image"
    image_preview.short_description = 'Preview'


@admin.register(RecentActivity)
class RecentActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_type_badge', 'title', 'date', 'order', 'is_visible']
    list_filter = ['activity_type', 'is_visible', 'date']
    list_editable = ['order', 'is_visible']
    search_fields = ['title', 'description']
    date_hierarchy = 'date'
    ordering = ['-date', 'order']
    
    fieldsets = (
        (None, {
            'fields': ('activity_type', 'title', 'description', 'date')
        }),
        ('Optional', {
            'fields': ('link',),
            'classes': ('collapse',),
        }),
        ('Display', {
            'fields': ('order', 'is_visible'),
        }),
    )
    
    def activity_type_badge(self, obj):
        colors = {
            'article': '#3b82f6',
            'project': '#10b981',
            'talk': '#8b5cf6',
            'achievement': '#f59e0b',
            'learning': '#ec4899',
            'other': '#6b7280',
        }
        color = colors.get(obj.activity_type, '#6b7280')
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; '
            'border-radius: 12px; font-size: 11px;">{}</span>',
            color,
            obj.get_activity_type_display()
        )
    activity_type_badge.short_description = 'Type'


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'updated_at', 'download_link']
    list_filter = ['is_active', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'resume_file', 'is_active'),
            'description': 'Upload your latest resume. Only one resume can be active at a time.'
        }),
        ('Optional Online Resume', {
            'fields': ('summary',),
            'classes': ('collapse',),
            'description': 'Optional: Add content for an HTML version of your resume'
        }),
    )
    
    def download_link(self, obj):
        if obj.resume_file:
            return format_html(
                '<a href="{}" target="_blank">Download PDF →</a>',
                obj.resume_file.url
            )
        return "No file"
    download_link.short_description = 'File'
    
    def save_model(self, request, obj, form, change):
        # Ensure only one active resume
        if obj.is_active:
            Resume.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at', 'is_read', 'status_badge']
    list_filter = ['is_read', 'submitted_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'submitted_at']
    date_hierarchy = 'submitted_at'
    actions = ['mark_as_read', 'mark_as_unread']

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'submitted_at')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
    )

    def status_badge(self, obj):
        if obj.is_read:
            return format_html(
                '<span style="background-color: #10b981; color: white; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 500;">Read</span>'
            )
        return format_html(
            '<span style="background-color: #2563eb; color: white; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 500;">New</span>'
        )
    status_badge.short_description = 'Status'

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} message(s) marked as read.")
    mark_as_read.short_description = "Mark selected as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, f"{queryset.count()} message(s) marked as unread.")
    mark_as_unread.short_description = "Mark selected as unread"


# ============================================
# ADMIN SITE CUSTOMIZATION
# ============================================

admin.site.site_header = "Ken Ruto Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to your Portfolio Dashboard"