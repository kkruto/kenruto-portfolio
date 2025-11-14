from django import forms
from .models import NewsletterSubscriber, ContactMessage

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'flex-1 px-6 py-3 rounded-full border-2 border-transparent focus:border-brand focus:outline-none focus:ring-4 focus:ring-brand/20 transition-all duration-200',
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'w-full px-4 py-3 rounded-lg border border-neutral-300 focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20 transition-all',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'w-full px-4 py-3 rounded-lg border border-neutral-300 focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20 transition-all',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about your project, idea, or just say hello...',
                'rows': 5,
                'class': 'w-full px-4 py-3 rounded-lg border border-neutral-300 focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20 transition-all resize-none',
            }),
        }