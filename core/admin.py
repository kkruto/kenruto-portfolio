from django.contrib import admin
from .models import NewsletterSubscriber, Experience, NowItem, Skill

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'type', 'start_date', 'is_current']
    list_filter = ['type', 'is_current']
    search_fields = ['title', 'organization', 'description']
    ordering = ['-start_date']

@admin.register(NowItem)
class NowItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    ordering = ['category', 'order']