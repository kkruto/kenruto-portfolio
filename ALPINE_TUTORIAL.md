# ALPINE.JS TUTORIAL FOR FRONTEND CONTRIBUTIONS

**For: Someone New to Alpine.js**
**Project: Ken Ruto Portfolio**
**Last Updated: 2025-01-14**

---

## 📚 TABLE OF CONTENTS

1. [What is Alpine.js?](#what-is-alpinejs)
2. [Why We Use Alpine.js](#why-we-use-alpinejs)
3. [How Alpine.js Works](#how-alpinejs-works)
4. [Core Concepts](#core-concepts)
5. [Common Directives](#common-directives)
6. [Real Examples from This Project](#real-examples-from-this-project)
7. [How to Add New Features](#how-to-add-new-features)
8. [Debugging Tips](#debugging-tips)
9. [Common Patterns](#common-patterns)
10. [Resources](#resources)

---

## 🎯 WHAT IS ALPINE.JS?

Alpine.js is a lightweight JavaScript framework that lets you add interactivity to HTML without writing complex JavaScript. Think of it as "jQuery for the modern web" or "Tailwind for JavaScript."

**Key Points:**
- No build step required (loaded via CDN)
- Write interactivity directly in HTML
- Reactive (updates automatically when data changes)
- Tiny (15KB gzipped)

**Example:**
```html
<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    <div x-show="open">I appear when open is true!</div>
</div>
```

That's it! No separate JavaScript file needed.

---

## 💡 WHY WE USE ALPINE.JS

### In This Project:
1. **Contact Form Modal** - Opens/closes when clicking "Get in Touch"
2. **Mobile Navigation** - Hamburger menu that slides in/out
3. **Collapsible Sections** - Resume dropdowns on About page
4. **Scroll-to-Top Button** - Shows/hides based on scroll position
5. **Newsletter Form** - Validation and loading states

### Why Not Use React/Vue?
- **Overkill** for this project (mostly static content)
- **No Build Step** - simpler deployment
- **Faster** - loads instantly
- **Easier to Learn** - HTML-first approach

---

## ⚙️ HOW ALPINE.JS WORKS

### 1. Alpine.js is Loaded via CDN (base.html)
```html
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

The `defer` attribute means "wait until the page loads before running."

### 2. Alpine.js Looks for Special Attributes
When the page loads, Alpine.js scans all HTML for attributes starting with `x-`:
- `x-data` - Creates a component with state
- `x-show` - Shows/hides elements
- `x-if` - Conditionally renders elements
- `@click` - Handles click events
- `x-model` - Two-way data binding

### 3. It Makes Everything Reactive
When data changes, the page updates automatically.

---

## 🧩 CORE CONCEPTS

### Concept #1: Components (x-data)

Every Alpine.js feature starts with `x-data`, which creates a **component** with its own **state**.

```html
<div x-data="{ count: 0, name: 'Ken' }">
    <!-- This div is now a component -->
    <!-- It has state: count=0, name='Ken' -->
</div>
```

**State** = data that can change (variables)

### Concept #2: Directives

Directives are special HTML attributes that tell Alpine what to do.

| Directive | Purpose | Example |
|-----------|---------|---------|
| `x-data` | Create component state | `x-data="{ open: false }"` |
| `x-show` | Show/hide element | `x-show="open"` |
| `@click` | Handle click event | `@click="open = true"` |
| `x-model` | Two-way binding | `x-model="email"` |
| `x-text` | Set text content | `x-text="name"` |
| `:class` | Dynamic classes | `:class="open && 'active'"` |

### Concept #3: Scope

State from `x-data` is available to **all child elements** but not siblings or parents.

```html
<div x-data="{ message: 'Hello' }">
    <p x-text="message"></p>  <!-- ✅ Works: Hello -->
</div>
<p x-text="message"></p>  <!-- ❌ Error: message not defined -->
```

---

## 📋 COMMON DIRECTIVES

### 1. `x-data` - Create Component State

**Syntax:**
```html
<div x-data="{ key: value, key2: value2 }">
```

**Example:**
```html
<div x-data="{
    name: '',
    email: '',
    submitted: false
}">
    <!-- Component with 3 state variables -->
</div>
```

**With Functions:**
```html
<div x-data="{
    count: 0,
    increment() {
        this.count++;
    }
}">
    <button @click="increment()">Count: <span x-text="count"></span></button>
</div>
```

---

### 2. `x-show` - Show/Hide Elements

**Syntax:**
```html
<div x-show="condition">Content</div>
```

**How it works:**
- `true` → element visible (display: block)
- `false` → element hidden (display: none)

**Example:**
```html
<div x-data="{ visible: false }">
    <button @click="visible = !visible">Toggle</button>
    <div x-show="visible">Now you see me!</div>
</div>
```

**With Transitions:**
```html
<div x-show="open" x-transition>
    <!-- Smooth fade in/out -->
</div>
```

---

### 3. `@click` - Handle Click Events

**Syntax:**
```html
<button @click="action">Click me</button>
```

**Examples:**
```html
<!-- Set a variable -->
<button @click="open = true">Open</button>

<!-- Toggle a variable -->
<button @click="open = !open">Toggle</button>

<!-- Call a function -->
<button @click="submitForm()">Submit</button>

<!-- Multiple actions -->
<button @click="count++; saveCount()">Increment</button>
```

**Prevent Default:**
```html
<form @submit.prevent="handleSubmit()">
    <!-- Prevents page reload -->
</form>
```

**Click Outside:**
```html
<div @click.away="open = false">
    <!-- Closes when clicking outside -->
</div>
```

---

### 4. `x-model` - Two-Way Data Binding

**Syntax:**
```html
<input x-model="variableName">
```

**How it works:**
- Typing in input → updates variable
- Variable changes → updates input

**Example:**
```html
<div x-data="{ email: '' }">
    <input type="email" x-model="email" placeholder="Your email">
    <p>You entered: <span x-text="email"></span></p>
</div>
```

As you type, the `<p>` updates in real-time!

---

### 5. `:class` - Dynamic CSS Classes

**Syntax:**
```html
<div :class="condition && 'class-name'">
```

**Examples:**
```html
<!-- Add class when condition is true -->
<div :class="open && 'bg-blue-500'">

<!-- Add different classes based on condition -->
<div :class="active ? 'text-blue' : 'text-gray'">

<!-- Add multiple classes -->
<div :class="{ 'font-bold': selected, 'text-red': error }">
```

---

### 6. `x-text` - Set Text Content

**Syntax:**
```html
<p x-text="variableName"></p>
```

**Example:**
```html
<div x-data="{ count: 0 }">
    <button @click="count++">Increment</button>
    <p>Count: <span x-text="count"></span></p>
</div>
```

---

### 7. `x-if` - Conditional Rendering

**Syntax:**
```html
<template x-if="condition">
    <div>Content</div>
</template>
```

**Difference from x-show:**
- `x-show` → hides element (display: none)
- `x-if` → removes element from DOM completely

**When to use:**
- `x-show` → frequently toggled elements
- `x-if` → rarely shown, heavy elements

---

## 🏗️ REAL EXAMPLES FROM THIS PROJECT

### Example 1: Contact Form Modal

**File:** `templates/components/contact_modal.html`

```html
<div
    x-data="{
        open: false,
        name: '',
        email: '',
        message: '',
        loading: false,
        error: ''
    }"
    @open-contact-modal.window="open = true; document.body.style.overflow = 'hidden';"
>
    <!-- Modal Content -->
    <div x-show="open" x-transition>
        <form @submit="validateAndSubmit()">
            <input x-model="name" type="text" placeholder="Name">
            <input x-model="email" type="email" placeholder="Email">
            <textarea x-model="message" placeholder="Message"></textarea>

            <div x-show="error" x-text="error"></div>

            <button type="submit" :disabled="loading">
                <span x-show="!loading">Send</span>
                <span x-show="loading">Sending...</span>
            </button>
        </form>
    </div>
</div>
```

**How it works:**
1. `x-data` creates component with state
2. `@open-contact-modal.window` listens for custom event
3. `x-show="open"` shows modal when open=true
4. `x-model` binds form inputs to state
5. `x-show="loading"` shows loading spinner
6. `:disabled="loading"` disables button while submitting

**To trigger the modal from anywhere:**
```html
<button @click="$dispatch('open-contact-modal')">Get in Touch</button>
```

---

### Example 2: Collapsible Resume Sections

**File:** `templates/about.html`

```html
{% if experiences %}
<div x-data="{ open: false }">
    <button
        @click="open = !open"
        class="w-full flex items-center justify-between p-5"
    >
        <h3>Experience</h3>
        <svg :class="open && 'rotate-180'">
            <!-- Arrow icon -->
        </svg>
    </button>

    <div x-show="open" x-transition class="p-5">
        <!-- Experience content -->
        {% for exp in experiences %}
            <div>{{ exp.title }}</div>
        {% endfor %}
    </div>
</div>
{% endif %}
```

**How it works:**
1. `x-data="{ open: false }"` → section closed by default
2. `@click="open = !open"` → toggles open/closed
3. `:class="open && 'rotate-180'"` → rotates arrow when open
4. `x-show="open"` → shows content when open
5. `x-transition` → smooth animation

---

### Example 3: Scroll-to-Top Button

**File:** `templates/base.html`

```html
<button
    x-data="{ show: false }"
    @scroll.window="show = (window.pageYOffset > 300)"
    x-show="show"
    x-transition
    @click="window.scrollTo({ top: 0, behavior: 'smooth' })"
    class="fixed bottom-8 right-8 bg-accent text-white p-3 rounded-full"
>
    <!-- Up arrow icon -->
</button>
```

**How it works:**
1. `x-data="{ show: false }"` → button hidden by default
2. `@scroll.window` → listens for page scroll
3. `show = (window.pageYOffset > 300)` → show after scrolling 300px
4. `x-show="show"` → shows/hides button
5. `@click="window.scrollTo(...)"` → scrolls to top smoothly

---

### Example 4: Mobile Navigation

**File:** `templates/components/nav.html`

```html
<nav x-data="{ mobileMenuOpen: false }">
    <!-- Hamburger Button -->
    <button @click="mobileMenuOpen = !mobileMenuOpen">
        <svg x-show="!mobileMenuOpen">☰</svg>
        <svg x-show="mobileMenuOpen">✕</svg>
    </button>

    <!-- Mobile Menu -->
    <div
        x-show="mobileMenuOpen"
        x-transition
        @click.away="mobileMenuOpen = false"
        class="mobile-menu"
    >
        <a href="/" @click="mobileMenuOpen = false">Home</a>
        <a href="/about" @click="mobileMenuOpen = false">About</a>
    </div>
</nav>
```

**How it works:**
1. `x-data` creates menu state
2. Hamburger button toggles menu
3. `@click.away` closes menu when clicking outside
4. Links close menu after clicking

---

## 🛠️ HOW TO ADD NEW FEATURES

### Step 1: Identify What You Need

Ask yourself:
- Do I need to show/hide something? → `x-show`
- Do I need to track user input? → `x-model`
- Do I need to respond to clicks? → `@click`
- Do I need to store state? → `x-data`

### Step 2: Create the Component

Start with `x-data`:

```html
<div x-data="{ /* your state here */ }">
    <!-- your feature here -->
</div>
```

### Step 3: Add Interactivity

Add directives to make it work:

```html
<div x-data="{ visible: false }">
    <button @click="visible = true">Show</button>
    <div x-show="visible">Content</div>
</div>
```

---

## 🎓 PRACTICAL EXAMPLE: Add a "Read More" Button

Let's add a "Read More" button to truncated text.

### Before:
```html
<div>
    <p>This is a very long piece of text that should be truncated...</p>
</div>
```

### After:
```html
<div x-data="{ expanded: false }">
    <p :class="!expanded && 'line-clamp-3'">
        This is a very long piece of text that should be truncated but you can expand it to read more if you want to see the full content here.
    </p>
    <button @click="expanded = !expanded" class="text-accent text-sm mt-2">
        <span x-show="!expanded">Read more</span>
        <span x-show="expanded">Read less</span>
    </button>
</div>
```

**Explanation:**
1. `x-data="{ expanded: false }"` → tracks if text is expanded
2. `:class="!expanded && 'line-clamp-3'"` → limits to 3 lines when collapsed
3. `@click="expanded = !expanded"` → toggles expanded state
4. `x-show` conditionally shows "Read more" or "Read less"

---

## 🐛 DEBUGGING TIPS

### 1. Check Console for Errors

Open browser DevTools (F12) and check Console tab for errors.

### 2. Use `console.log()` in Alpine

```html
<div x-data="{ count: 0 }">
    <button @click="count++; console.log('Count is:', count)">
        Increment
    </button>
</div>
```

### 3. Check if Alpine is Loaded

In browser console, type:
```javascript
Alpine.version
```

Should show version number (e.g., "3.13.3")

### 4. Common Errors

**Error: "Cannot read property of undefined"**
- Forgot to define variable in `x-data`
- Typo in variable name

**Error: "Alpine is not defined"**
- Alpine.js script not loaded
- Script loaded before Alpine initializes (use `defer`)

**Element not showing up:**
- Check `x-show` condition
- Check if `display: none` is in CSS
- Use browser DevTools to inspect element

---

## 📦 COMMON PATTERNS

### Pattern 1: Toggle Anything

```html
<div x-data="{ active: false }">
    <button @click="active = !active">Toggle</button>
    <div x-show="active">Toggleable content</div>
</div>
```

### Pattern 2: Form with Validation

```html
<form
    x-data="{ email: '', error: '' }"
    @submit.prevent="
        if (!email.includes('@')) {
            error = 'Invalid email';
        } else {
            $el.submit();
        }
    "
>
    <input x-model="email" type="email" required>
    <p x-show="error" x-text="error" class="text-red-500"></p>
    <button type="submit">Submit</button>
</form>
```

### Pattern 3: Tabs

```html
<div x-data="{ tab: 'home' }">
    <button @click="tab = 'home'" :class="tab === 'home' && 'active'">Home</button>
    <button @click="tab = 'about'" :class="tab === 'about' && 'active'">About</button>

    <div x-show="tab === 'home'">Home content</div>
    <div x-show="tab === 'about'">About content</div>
</div>
```

### Pattern 4: Dropdown Menu

```html
<div x-data="{ open: false }">
    <button @click="open = !open">Menu</button>
    <div
        x-show="open"
        @click.away="open = false"
        class="dropdown"
    >
        <a href="#">Option 1</a>
        <a href="#">Option 2</a>
    </div>
</div>
```

### Pattern 5: Loading State

```html
<div x-data="{ loading: false }">
    <button
        @click="loading = true; setTimeout(() => loading = false, 2000)"
        :disabled="loading"
    >
        <span x-show="!loading">Click me</span>
        <span x-show="loading">Loading...</span>
    </button>
</div>
```

---

## 📚 RESOURCES

### Official Docs:
- **Alpine.js Docs**: https://alpinejs.dev
- **Cheat Sheet**: https://alpinejs.dev/start-here

### This Project:
- **Examples**: All templates in `/templates/`
- **Best Example**: `/templates/components/contact_modal.html`
- **Complex Example**: `/templates/components/nav.html`

### Learning Path:
1. Read this tutorial
2. Look at `/templates/components/contact_modal.html`
3. Try modifying the contact form
4. Create a simple feature (like "Read More" button)
5. Reference official docs when stuck

---

## 🎯 QUICK REFERENCE

| Want to... | Use... | Example |
|-----------|--------|---------|
| Create state | `x-data` | `x-data="{ count: 0 }"` |
| Show/hide | `x-show` | `x-show="visible"` |
| Handle click | `@click` | `@click="count++"` |
| Bind input | `x-model` | `x-model="email"` |
| Dynamic class | `:class` | `:class="active && 'bg-blue'"` |
| Set text | `x-text` | `x-text="message"` |
| Loop data | `x-for` | `<template x-for="item in items">` |
| Conditional | `x-if` | `<template x-if="show">` |
| Disable button | `:disabled` | `:disabled="loading"` |
| Smooth transition | `x-transition` | `x-show="open" x-transition` |

---

## 🚀 NEXT STEPS

1. **Practice**: Try adding a new feature to the site
2. **Read Code**: Look at existing Alpine.js in templates
3. **Experiment**: Change values and see what happens
4. **Ask**: Check official docs or search for examples

**Remember:** Alpine.js is all about making HTML interactive with minimal JavaScript. If it feels complicated, you're probably overthinking it!

---

**Questions? Check the templates folder for real examples!**
