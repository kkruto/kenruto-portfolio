from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import NewsletterSubscriber, Experience, NowItem, Skill
from .forms import NewsletterForm

def home(request):
    """Homepage with portal cards"""
    return render(request, 'home.html')

def about(request):
    """About page with full professional bio"""
    context = {
        'now_items': NowItem.objects.filter(is_active=True),
        'experiences': Experience.objects.filter(type='work'),
        'skills': Skill.objects.all(),
    }
    return render(request, 'about.html', context)

def tlw_studio(request):
    """The Lion Writes Studio placeholder"""
    return render(request, 'tlw.html')

def small_bets(request):
    """Small Bets placeholder"""
    return render(request, 'small_bets.html')

def kiota(request):
    """Kiota blog placeholder"""
    return render(request, 'kiota.html')

def gallery(request):
    """Gallery placeholder"""
    return render(request, 'gallery.html')

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