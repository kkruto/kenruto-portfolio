// Wait for Alpine to be ready
document.addEventListener('alpine:init', () => {
  console.log('Alpine.js initialized');
  
  // Global navigation store
  Alpine.store('navigation', {
    transitioning: false,
    currentPage: window.location.pathname,
    
    navigate(url) {
      this.transitioning = true;
      setTimeout(() => {
        window.location.href = url;
      }, 300);
    }
  });
  
  // Mobile menu store
  Alpine.store('menu', {
    open: false,
    
    toggle() {
      this.open = !this.open;
      console.log('Menu toggled:', this.open);
    },
    
    close() {
      this.open = false;
    }
  });
  
  // Newsletter form component
  Alpine.data('newsletterForm', () => ({
    email: '',
    loading: false,
    
    init() {
      console.log('Newsletter form initialized');
    },
    
    submit() {
      if (!this.email) {
        alert('Please enter your email');
        return false;
      }
      this.loading = true;
      return true;
    }
  }));
  
  // Smooth scroll magic
  Alpine.magic('scrollTo', () => {
    return (selector) => {
      const element = document.querySelector(selector);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };
  });
});

// Intersection Observer for fade-in animations
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM loaded, setting up observers');
  
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-fade-in');
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe all elements with fade-on-scroll class
  const fadeElements = document.querySelectorAll('.fade-on-scroll');
  console.log('Found fade elements:', fadeElements.length);
  
  fadeElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    observer.observe(el);
  });
});

// Add smooth hover effects to portal cards
document.addEventListener('DOMContentLoaded', () => {
  const portalCards = document.querySelectorAll('.portal-card');
  
  portalCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-8px)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
});