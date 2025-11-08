/**
 * ============================================
 * ALPINE.JS SETUP & CONFIGURATION
 * ============================================
 * 
 * Alpine.js is a minimal JavaScript framework that adds interactivity
 * to your HTML without writing complex JavaScript.
 * 
 * Think of it as "Tailwind for JavaScript" - you add functionality
 * directly in your HTML using special attributes.
 */

// Wait for the DOM to be fully loaded before initializing
document.addEventListener('DOMContentLoaded', function() {
  console.log('🏔️ Alpine.js is ready!');
});

/**
 * ============================================
 * ALPINE.JS CHEAT SHEET FOR YOUR REFERENCE
 * ============================================
 * 
 * 1. x-data="{ key: value }"
 *    - Declares a component's reactive state
 *    - Example: <div x-data="{ open: false }">
 * 
 * 2. x-show="condition"
 *    - Toggle visibility (element stays in DOM)
 *    - Example: <div x-show="open">Content</div>
 * 
 * 3. x-if="condition"
 *    - Conditional rendering (element removed from DOM)
 *    - Must be on a <template> tag
 *    - Example: <template x-if="open"><div>Content</div></template>
 * 
 * 4. @click="action"
 *    - Shorthand for x-on:click
 *    - Handle click events
 *    - Example: <button @click="open = !open">Toggle</button>
 * 
 * 5. :class="condition"
 *    - Shorthand for x-bind:class
 *    - Dynamic class binding
 *    - Example: <div :class="open ? 'block' : 'hidden'">
 * 
 * 6. x-transition
 *    - Smooth transitions when showing/hiding
 *    - Example: <div x-show="open" x-transition>
 * 
 * 7. x-model="variable"
 *    - Two-way data binding for inputs
 *    - Example: <input x-model="email">
 * 
 * 8. x-text="expression"
 *    - Update element's text content
 *    - Example: <span x-text="count"></span>
 * 
 * 9. x-html="expression"
 *    - Update element's HTML content
 *    - Example: <div x-html="content"></div>
 * 
 * 10. x-for="item in items"
 *     - Loop through arrays
 *     - Example: <template x-for="item in list"><li x-text="item"></li></template>
 */

/**
 * ============================================
 * GLOBAL ALPINE.JS STORES (Optional)
 * ============================================
 * 
 * You can create global state that's accessible across all components:
 */

// Example: Global state store (uncomment if needed)
/*
document.addEventListener('alpine:init', () => {
  Alpine.store('navigation', {
    currentPath: window.location.pathname,
    isScrolled: false,
    
    init() {
      // Track scroll position
      window.addEventListener('scroll', () => {
        this.isScrolled = window.scrollY > 50;
      });
    }
  });
});
*/

/**
 * ============================================
 * UTILITY FUNCTIONS
 * ============================================
 */

// Smooth scroll to element
function scrollToElement(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Copy text to clipboard
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    console.log('✅ Copied to clipboard');
  }).catch(err => {
    console.error('❌ Failed to copy:', err);
  });
}

/**
 * ============================================
 * PAGE TRANSITION EFFECTS
 * ============================================
 */

// Add fade-in effect to page content
window.addEventListener('load', () => {
  const content = document.querySelector('.page-transition');
  if (content) {
    content.style.opacity = '0';
    setTimeout(() => {
      content.style.opacity = '1';
    }, 100);
  }
});

/**
 * ============================================
 * FORM HANDLING UTILITIES
 * ============================================
 */

// Handle newsletter form submission
function handleNewsletterSubmit(event) {
  // The form will be submitted normally to Django
  // You can add additional client-side validation here if needed
  const email = event.target.querySelector('input[type="email"]').value;
  
  if (!email || !email.includes('@')) {
    event.preventDefault();
    alert('Please enter a valid email address');
    return false;
  }
  
  return true;
}

/**
 * ============================================
 * ACCESSIBILITY HELPERS
 * ============================================
 */

// Trap focus within modal/menu (for accessibility)
function trapFocus(element) {
  const focusableElements = element.querySelectorAll(
    'a[href], button:not([disabled]), textarea, input, select'
  );
  
  const firstFocusable = focusableElements[0];
  const lastFocusable = focusableElements[focusableElements.length - 1];
  
  element.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstFocusable) {
        e.preventDefault();
        lastFocusable.focus();
      } else if (!e.shiftKey && document.activeElement === lastFocusable) {
        e.preventDefault();
        firstFocusable.focus();
      }
    }
  });
}

/**
 * ============================================
 * CONSOLE MESSAGE
 * ============================================
 */

console.log(`
╔═══════════════════════════════════════╗
║   🏔️  ALPINE.JS LOADED SUCCESSFULLY  ║
║                                       ║
║   Your interactive components are     ║
║   now ready to use!                   ║
╚═══════════════════════════════════════╝
`);