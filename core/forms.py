from django import forms
from .models import NewsletterSubscriber

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