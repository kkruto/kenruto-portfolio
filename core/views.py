# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import (
    NewsletterSubscriber, 
    Experience, 
    NowItem, 
    Skill,
    Article,
    GalleryItem,
    RecentActivity,
    Resume
)
from .forms import NewsletterForm


def home(request):
    """
    Enhanced homepage with:
    - What I'm Doing Now
    - Recent Activities
    - Featured/Recent Articles
    - Previously (work experience)
    """
    context = {
        # What I'm doing now
        'now_items': NowItem.objects.filter(is_active=True)[:3],
        
        # Recent activities
        'recent_activities': RecentActivity.objects.filter(is_visible=True)[:5],
        
        # Featured or recent articles
        'featured_articles': Article.objects.filter(
            status='published',
            is_featured=True
        )[:3],
        
        'recent_articles': Article.objects.filter(
            status='published'
        ).order_by('-published_date')[:6],
        
        # Previously (recent work experience)
        'recent_experiences': Experience.objects.filter(type='work')[:3],
    }
    return render(request, 'home.html', context)


def about(request):
    """About page with full professional bio"""
    context = {
        'now_items': NowItem.objects.filter(is_active=True),
        'experiences': Experience.objects.filter(type='work'),
        'education': Experience.objects.filter(type='education'),
        'skills': Skill.objects.all(),
        'resume': Resume.objects.filter(is_active=True).first(),  # Active resume
    }
    return render(request, 'about.html', context)


def kiota(request):
    """Essays listing page - all published articles"""
    articles = Article.objects.filter(status='published').order_by('-published_date')
    
    # Optional: Filter by type
    article_type = request.GET.get('type')
    if article_type:
        articles = articles.filter(article_type=article_type)
    
    # Optional: Search
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) | 
            Q(excerpt__icontains=query) |
            Q(content__icontains=query)
        )
    
    context = {
        'articles': articles,
        'article_types': Article.ARTICLE_TYPES,
        'selected_type': article_type,
        'search_query': query,
    }
    return render(request, 'kiota.html', context)


def article_detail(request, slug):
    """Individual article/essay page"""
    article = get_object_or_404(Article, slug=slug, status='published')
    
    # Get related articles (same type or similar tags)
    related_articles = Article.objects.filter(
        status='published'
    ).exclude(id=article.id)
    
    # Prioritize same type
    if article.article_type:
        related_articles = related_articles.filter(
            article_type=article.article_type
        )
    
    related_articles = related_articles[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'article_detail.html', context)


def small_bets(request):
    """Projects/Small Bets page"""
    # You can add Project model later, for now keeping simple
    return render(request, 'small_bets.html')


def tlw_studio(request):
    """The Lion Writes Studio page"""
    return render(request, 'tlw.html')


def gallery(request):
    """Gallery page with photos/artwork"""
    gallery_items = GalleryItem.objects.filter(is_visible=True)
    
    # Optional: Filter by type
    gallery_type = request.GET.get('type')
    if gallery_type:
        gallery_items = gallery_items.filter(gallery_type=gallery_type)
    
    context = {
        'gallery_items': gallery_items,
        'gallery_types': GalleryItem.GALLERY_TYPES,
        'selected_type': gallery_type,
    }
    return render(request, 'gallery.html', context)


def resume(request):
    """Resume/CV page"""
    active_resume = Resume.objects.filter(is_active=True).first()
    
    context = {
        'resume': active_resume,
        'experiences': Experience.objects.filter(type='work'),
        'education': Experience.objects.filter(type='education'),
        'skills': Skill.objects.all(),
    }
    return render(request, 'resume.html', context)


@require_http_methods(["POST"])
def newsletter_subscribe(request):
    """Handle newsletter subscription"""
    form = NewsletterForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
        
        if created:
            messages.success(request, 'Successfully subscribed to the newsletter!')
        else:
            if subscriber.is_active:
                messages.info(request, 'You\'re already subscribed!')
            else:
                subscriber.is_active = True
                subscriber.save()
                messages.success(request, 'Welcome back! You\'re subscribed again.')
    else:
        messages.error(request, 'Please enter a valid email address.')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))