# CLAUDE.md - AI Assistant Guide for kenruto-portfolio

**Last Updated:** 2025-11-14
**Project Version:** MVP V 0.1
**Maintainer:** Ken Ruto

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Directory Structure](#directory-structure)
4. [Development Setup](#development-setup)
5. [Architecture & Design Patterns](#architecture--design-patterns)
6. [Database Models](#database-models)
7. [Template System](#template-system)
8. [Frontend Architecture](#frontend-architecture)
9. [Development Workflows](#development-workflows)
10. [Code Conventions](#code-conventions)
11. [Common Tasks](#common-tasks)
12. [Production Considerations](#production-considerations)
13. [Important Files Reference](#important-files-reference)

---

## Project Overview

**kenruto-portfolio** is a personal portfolio website for Ken Ruto, showcasing his work as a Product Manager, Engineer, and Writer. The project emphasizes clean design, educational code documentation, and simplicity.

### Purpose
- Display professional experience, projects, and skills
- Publish essays and visual/data essays
- Share photography and design work
- Provide downloadable resume/CV
- Collect newsletter subscriptions

### Current Status
- **Stage:** MVP V 0.1 completed
- **Environment:** Development mode
- **Production Ready:** No (requires configuration)

---

## Tech Stack

### Backend
- **Django 5.2.7** - Python web framework
- **SQLite3** - Database (development)
- **WhiteNoise** - Static file serving
- **Python 3.x** - Runtime environment

### Frontend
- **Tailwind CSS 3.3.5** - Utility-first CSS framework
  - `@tailwindcss/typography` - Rich text styling
  - `@tailwindcss/forms` - Form component styling
- **Alpine.js 3.13.3** - Lightweight JavaScript framework (CDN-loaded)

### Build Tools
- **Node.js/NPM** - Frontend dependency management
- **Tailwind CLI** - CSS compilation

### Deployment Stack
- **WSGI/ASGI** ready
- **WhiteNoise** with `CompressedManifestStaticFilesStorage`

---

## Directory Structure

```
kenruto-portfolio/
├── manage.py                      # Django management script
├── package.json                   # Node.js dependencies
├── package-lock.json             # Node lock file
├── tailwind.config.js            # Tailwind configuration
├── db.sqlite3                    # SQLite database (gitignored)
│
├── portfolio/                     # Django project configuration
│   ├── settings.py               # Main settings (TIME_ZONE: Africa/Nairobi)
│   ├── urls.py                   # Root URL routing
│   ├── wsgi.py                   # WSGI entry point
│   └── asgi.py                   # ASGI entry point
│
├── core/                         # Main Django application
│   ├── models.py                 # 7 models (326 lines)
│   ├── views.py                  # 8 view functions (175 lines)
│   ├── admin.py                  # Customized admin (302 lines)
│   ├── forms.py                  # Django forms
│   ├── urls.py                   # App URL routing
│   └── migrations/               # Database migrations
│
├── templates/                    # Django templates
│   ├── base.html                 # Base layout (extends all pages)
│   ├── home.html                 # Homepage
│   ├── about.html                # About page
│   ├── resume.html               # Resume/CV page
│   ├── kiota.html                # Essays listing
│   ├── article_detail.html       # Individual article
│   ├── gallery.html              # Photo gallery
│   ├── small_bets.html           # Projects page
│   ├── tlw.html                  # TLW Studio page
│   └── components/               # Reusable components
│       ├── nav.html              # Navigation (186 lines)
│       ├── footer.html           # Footer (80 lines)
│       └── newsletter.html       # Newsletter form (159 lines)
│
└── static/                       # Static assets
    ├── css/
    │   ├── input.css             # Tailwind source (193 lines)
    │   └── output.css            # Compiled CSS (gitignored)
    └── js/
        └── app.js                # Custom JavaScript (194 lines)
```

### Important Gitignored Items
- `db.sqlite3` - Database file
- `media/` - Uploaded files (images, PDFs)
- `staticfiles/` - Collected static files
- `static/css/output.css` - Generated Tailwind CSS
- `node_modules/` - NPM dependencies
- `__pycache__/`, `*.pyc` - Python bytecode
- `.env` - Environment variables

---

## Development Setup

### Prerequisites
```bash
# Required
- Python 3.x
- Node.js and NPM
- pip (Python package manager)

# Recommended
- Virtual environment (venv)
- SQLite3
```

### Initial Setup

1. **Clone and navigate to repository:**
   ```bash
   cd /home/user/kenruto-portfolio
   ```

2. **Create virtual environment (if not exists):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install django whitenoise
   # Note: requirements.txt does not exist yet - should be created
   ```

4. **Install Node dependencies:**
   ```bash
   npm install
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser for admin access:**
   ```bash
   python manage.py createsuperuser
   ```

### Running Development Environment

**Terminal 1 - Tailwind CSS (watch mode):**
```bash
npm run dev
# Watches static/css/input.css
# Compiles to static/css/output.css on changes
```

**Terminal 2 - Django Development Server:**
```bash
python manage.py runserver
# Starts server at http://localhost:8000
# Admin interface at http://localhost:8000/admin
```

### Building for Production

```bash
# Compile and minify CSS
npm run build

# Collect static files
python manage.py collectstatic --noinput
```

---

## Architecture & Design Patterns

### Design Philosophy

**Minimalist & Content-Focused:**
- Neutral grayscale color palette (50-900)
- Single accent color (blue #2563eb)
- System fonts (no external font loading)
- Generous whitespace
- Clean, professional aesthetic

### Backend Patterns

**Fat Models, Thin Views:**
- Business logic lives in models
- Views coordinate between models and templates
- Example: `Article` model auto-generates slugs from titles
- Example: `Resume` model enforces "only one active resume" rule

**Function-Based Views (FBV):**
- All views use function-based pattern (not class-based)
- Simple, explicit, easy to understand
- Sufficient for current project complexity

**Django Admin Customization:**
- Heavily customized for content management
- Color-coded status badges
- Image preview thumbnails
- Batch actions (publish, draft, feature)
- Custom branding: "Ken Ruto Portfolio Admin"

### Frontend Patterns

**Component-Based Templates:**
- All pages extend `base.html`
- Reusable components in `templates/components/`
- DRY principle for navigation, footer, forms

**Progressive Enhancement:**
- Works without JavaScript
- Enhanced with Alpine.js for interactivity
- No critical functionality depends on JS

**Mobile-First Responsive:**
- Tailwind's mobile-first breakpoints
- Responsive navigation with mobile menu
- Touch-friendly interactions

### Content Management Patterns

**Status Workflows:**
- Draft → Published → Archived
- `is_active` / `is_visible` for soft deletes
- Featured content flags for highlighting

**Manual Ordering:**
- Most models include `order` field
- Allows curator control over display sequence

**Flexible Data Storage:**
- JSON fields for dynamic data (tags, tech_stack, achievements)
- Avoids over-normalization for simple lists

---

## Database Models

### Overview
Location: `/home/user/kenruto-portfolio/core/models.py` (326 lines)

The project has **7 database models** representing different content types:

### 1. NewsletterSubscriber
**Purpose:** Email subscription management

**Fields:**
- `email` (EmailField, unique) - Subscriber email
- `subscribed_at` (DateTimeField, auto_now_add) - Subscription timestamp
- `is_active` (BooleanField, default=True) - Subscription status

**Key Methods:**
- `__str__()` - Returns email

**Admin:** Basic list display with email and subscription date

---

### 2. Experience
**Purpose:** Work history, education, projects, awards

**Fields:**
- `type` (CharField, choices) - work | project | education | award
- `title` (CharField, 200) - Position/degree/project name
- `organization` (CharField, 200) - Company/school/organization
- `location` (CharField, 100, optional) - City, Country
- `start_date` (DateField) - Start date
- `end_date` (DateField, optional, blank=True) - End date (null = current)
- `description` (TextField) - Role/project description
- `achievements` (JSONField, default=list) - List of bullet points
- `tech_stack` (JSONField, default=list) - Technologies used
- `is_visible` (BooleanField, default=True) - Display toggle
- `order` (IntegerField, default=0) - Manual ordering
- `created_at`, `updated_at` - Timestamps

**Ordering:** `-start_date` (most recent first)

**Display Logic:**
- Current roles: `end_date is None`
- Duration calculations in templates

---

### 3. NowItem
**Purpose:** "What I'm Doing Now" section on homepage

**Fields:**
- `title` (CharField, 200) - Activity title
- `icon` (CharField, 10) - Emoji icon
- `description` (TextField) - What you're working on
- `link` (URLField, optional) - Related URL
- `order` (IntegerField, default=0) - Display order
- `is_active` (BooleanField, default=True) - Visibility toggle

**Ordering:** `order` (ascending)

**Usage:** Homepage displays active items in order

---

### 4. Skill
**Purpose:** Skills categorization for about/resume pages

**Fields:**
- `category` (CharField, choices) - product | engineering | leadership | design
- `name` (CharField, 100) - Skill name
- `order` (IntegerField, default=0) - Display order within category

**Ordering:** `category`, `order`

**Display:** Grouped by category in templates

---

### 5. Article (COMPLEX MODEL - 27 fields)
**Purpose:** Blog posts, essays, visual essays, tutorials

**Core Fields:**
- `title` (CharField, 300) - Article title
- `slug` (SlugField, unique, auto-generated) - URL slug
- `excerpt` (TextField, 500) - Short summary
- `content` (TextField) - Main content (supports Markdown)
- `article_type` (CharField, choices) - essay | visual_essay | data_essay | tutorial | case_study
- `status` (CharField, choices) - draft | published | archived

**Media Fields:**
- `featured_image` (ImageField, optional) - Main article image
- `featured_image_alt` (CharField, 200) - Alt text for accessibility

**Metadata Fields:**
- `read_time` (IntegerField) - Estimated minutes to read
- `published_at` (DateTimeField, optional) - Publication timestamp
- `tags` (CharField, 200, optional) - Comma-separated tags

**Interactive Content:**
- `has_interactive_content` (BooleanField) - Charts/graphs flag
- `custom_css` (TextField, optional) - Article-specific styles
- `custom_js` (TextField, optional) - Article-specific JavaScript

**SEO Fields:**
- `meta_description` (CharField, 160, optional)
- `meta_keywords` (CharField, 200, optional)

**Display Flags:**
- `is_featured` (BooleanField, default=False) - Featured content
- `show_in_feed` (BooleanField, default=True) - RSS/listing visibility

**Timestamps:**
- `created_at`, `updated_at`

**Key Methods:**
- `save()` - Auto-generates slug from title if not provided
- `get_related_articles()` - Returns similar articles by tags/type

**Ordering:** `-published_at` (newest first)

**Admin Features:**
- Rich fieldsets (Content, Media, Interactive, SEO, Publishing)
- Image preview for featured_image
- Batch actions: publish, draft, archive, feature
- Custom CSS/JS code editors

---

### 6. GalleryItem
**Purpose:** Photo gallery, design work, artwork

**Fields:**
- `title` (CharField, 200) - Item title
- `description` (TextField, optional) - Item description
- `image` (ImageField) - Main image (upload to gallery/)
- `thumbnail` (ImageField, optional) - Thumbnail (upload to gallery/thumbnails/)
- `item_type` (CharField, choices) - photo | design | art | project | other
- `tags` (JSONField, default=list) - Searchable tags
- `external_link` (URLField, optional) - Related URL
- `is_visible` (BooleanField, default=True)
- `order` (IntegerField, default=0)
- `uploaded_at` (DateTimeField, auto_now_add)

**Ordering:** `order`, `-uploaded_at`

**Admin:** Image preview with thumbnail generation support

---

### 7. Resume
**Purpose:** Resume/CV file management

**Fields:**
- `title` (CharField, 200, default="Resume") - Resume version name
- `resume_file` (FileField) - PDF upload (resume/)
- `summary` (TextField, optional) - Brief professional summary
- `is_active` (BooleanField, default=False) - Active resume flag
- `uploaded_at` (DateTimeField, auto_now_add)
- `updated_at` (DateTimeField, auto_now)

**Key Methods:**
- `save()` - Enforces "only one active resume" rule
  - When setting `is_active=True`, sets all other resumes to `is_active=False`

**Usage:** Resume page fetches `Resume.objects.filter(is_active=True).first()`

---

## Template System

### Base Template
**File:** `/home/user/kenruto-portfolio/templates/base.html`

**Provides:**
- HTML structure with responsive viewport
- Meta tags (description, keywords, author)
- Tailwind CSS inclusion (`static/css/output.css`)
- Alpine.js CDN loading (defer)
- Navigation component (`{% include 'components/nav.html' %}`)
- Content block (`{% block content %}{% endblock %}`)
- Footer component (`{% include 'components/footer.html' %}`)
- Django messages display with Alpine.js dismiss functionality

**All templates must extend base:**
```django
{% extends 'base.html' %}
{% load static %}

{% block content %}
<!-- Your content here -->
{% endblock %}
```

### Reusable Components

#### 1. Navigation (`templates/components/nav.html`)
**Lines:** 186
**Features:**
- Responsive mobile menu
- Alpine.js state management
- Scroll detection for backdrop styling
- Active page highlighting
- Links: Home, About, Essays, Projects, Gallery, Resume

**Alpine.js State:**
```javascript
x-data="{ mobileMenuOpen: false, currentPath: '{{ request.path }}' }"
```

**Mobile Menu Toggle:**
```html
@click="mobileMenuOpen = !mobileMenuOpen"
@click.away="mobileMenuOpen = false"
```

**Active Link Detection:**
```html
:class="currentPath === '/' ? 'text-accent-600' : ''"
```

---

#### 2. Footer (`templates/components/footer.html`)
**Lines:** 80
**Features:**
- Social links (GitHub, LinkedIn, Twitter, Email)
- Copyright notice
- Back to top button
- Centered, minimal design

**Social Links:**
- GitHub: github.com/kkruto
- LinkedIn: linkedin.com/in/kennyruto
- Twitter: @KenRuto
- Email: kenruto[at]example.com (update with real email)

---

#### 3. Newsletter Form (`templates/components/newsletter.html`)
**Lines:** 159
**Features:**
- Email subscription form
- Alpine.js validation
- Loading states
- Inline error messages
- CSRF protection
- Success/error feedback

**Alpine.js State:**
```javascript
x-data="{
  email: '',
  loading: false,
  error: '',
  success: false
}"
```

**Form Submission:**
- POST to `/newsletter/subscribe/`
- Shows loading spinner during submission
- Displays Django messages on success/error
- Clears form on success

---

### Page Templates

#### Homepage (`templates/home.html`)
**Sections:**
- Hero with title and tagline
- "What I'm Doing Now" (NowItem queryset)
- Recent experiences (3 most recent)
- Featured articles (3 featured)
- Newsletter signup

#### About (`templates/about.html`)
**Sections:**
- Full bio
- Skills by category (Product, Engineering, Leadership, Design)
- Education
- Resume download link

#### Resume (`templates/resume.html`)
**Sections:**
- Professional summary
- Work experience
- Projects
- Education
- Skills
- Awards
- Download resume button

#### Essays (`templates/kiota.html`)
**Features:**
- Article type filtering (all, essay, visual_essay, data_essay, tutorial, case_study)
- Search functionality
- Article cards with featured images
- Read time display
- Tags display

#### Article Detail (`templates/article_detail.html`)
**Features:**
- Full article content
- Featured image
- Publication date and read time
- Tags
- Related articles (3 similar)
- Social sharing (placeholder)

#### Gallery (`templates/gallery.html`)
**Features:**
- Masonry grid layout
- Type filtering (all, photo, design, art, project, other)
- Lightbox/modal (placeholder)
- External link support

---

## Frontend Architecture

### Tailwind CSS

**Configuration:** `/home/user/kenruto-portfolio/tailwind.config.js`

**Content Paths:**
```javascript
content: [
  './templates/**/*.html',
  './static/js/**/*.js',
]
```

**Custom Theme:**
```javascript
theme: {
  extend: {
    colors: {
      neutral: { 50-900 },  // Grayscale palette
      accent: {
        light: '#3b82f6',
        DEFAULT: '#2563eb',
        dark: '#1d4ed8'
      }
    },
    maxWidth: {
      prose: '65ch',
      content: '720px'
    }
  }
}
```

**Plugins:**
- `@tailwindcss/typography` - For rich text content
- `@tailwindcss/forms` - For form styling

---

### Custom CSS Layers

**File:** `/home/user/kenruto-portfolio/static/css/input.css` (193 lines)

#### @layer base
Typography defaults, link styles, focus states

```css
@apply font-sans antialiased text-neutral-900 bg-neutral-50;
a { @apply text-accent hover:text-accent-dark transition-colors; }
```

#### @layer components
Reusable UI components:

- `.container-custom` - Content container with max-width
- `.btn`, `.btn-primary`, `.btn-secondary` - Button variants
- `.nav-link` - Navigation link styles
- `.card` - Card component
- `.section` - Section spacing
- `.prose-custom` - Enhanced typography for articles

#### @layer utilities
Helper classes:

- `.page-transition` - Page fade effects
- `.fade-in`, `.slide-up` - Animation classes
- `.text-gradient` - Gradient text effect
- `.hover-underline` - Animated underline on hover
- `.no-print` - Hide elements when printing

---

### Alpine.js Integration

**Version:** 3.13.3 (CDN-loaded)
**Loading:** `<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>`

**Usage Pattern:**
- Component-scoped state (not global)
- Inline in templates (no separate Alpine files)
- Heavily documented for educational purposes

**Common Directives Used:**

1. **x-data** - Component state
   ```html
   <div x-data="{ open: false }">
   ```

2. **@click** - Event handling
   ```html
   <button @click="open = !open">
   ```

3. **x-show** - Conditional visibility
   ```html
   <div x-show="open">
   ```

4. **:class** - Dynamic classes
   ```html
   <a :class="active ? 'text-accent' : ''">
   ```

5. **x-transition** - Smooth animations
   ```html
   <div x-show="open" x-transition>
   ```

6. **x-model** - Two-way binding
   ```html
   <input x-model="email">
   ```

7. **@click.away** - Click outside detection
   ```html
   <div @click.away="open = false">
   ```

**Complete Alpine.js documentation available in:**
- `/home/user/kenruto-portfolio/static/js/app.js` (65 lines of cheat sheet)
- Inline comments in navigation and newsletter components

---

### JavaScript Utilities

**File:** `/home/user/kenruto-portfolio/static/js/app.js` (194 lines)

**Includes:**
- Console art banner on page load
- Alpine.js cheat sheet (commented)
- Utility functions (placeholders)
- Form validation helpers
- Smooth scroll utilities

---

## Development Workflows

### Daily Development

1. **Start development servers:**
   ```bash
   # Terminal 1
   npm run dev

   # Terminal 2
   python manage.py runserver
   ```

2. **Access application:**
   - Frontend: http://localhost:8000
   - Admin: http://localhost:8000/admin

3. **Make changes:**
   - Edit templates → Auto-reload Django server
   - Edit `static/css/input.css` → Auto-compile Tailwind
   - Edit Python files → Auto-reload Django server

4. **Test changes:**
   - View in browser
   - Check console for errors
   - Validate responsive design
   - Test in admin interface

---

### Database Changes Workflow

When modifying models:

1. **Edit model:**
   ```python
   # In core/models.py
   class MyModel(models.Model):
       new_field = models.CharField(max_length=100)
   ```

2. **Create migration:**
   ```bash
   python manage.py makemigrations
   # Review generated migration file
   ```

3. **Apply migration:**
   ```bash
   python manage.py migrate
   ```

4. **Update admin (if needed):**
   ```python
   # In core/admin.py
   @admin.register(MyModel)
   class MyModelAdmin(admin.ModelAdmin):
       list_display = ['field1', 'new_field']
   ```

5. **Update views/templates:**
   - Add new field to forms
   - Display in templates
   - Update queries if needed

---

### Adding New Pages

1. **Create template:**
   ```bash
   # Create templates/my_page.html
   ```
   ```django
   {% extends 'base.html' %}
   {% load static %}

   {% block content %}
   <!-- Your content -->
   {% endblock %}
   ```

2. **Create view:**
   ```python
   # In core/views.py
   def my_page(request):
       context = {
           'data': MyModel.objects.all()
       }
       return render(request, 'my_page.html', context)
   ```

3. **Add URL route:**
   ```python
   # In core/urls.py
   path('my-page/', views.my_page, name='my_page'),
   ```

4. **Add navigation link:**
   ```django
   <!-- In templates/components/nav.html -->
   <a href="{% url 'my_page' %}">My Page</a>
   ```

---

### Git Workflow

**Current Branch:** `claude/claude-md-mhyga4mpr1ck7iv4-01JMA64pL1haXBAmc1kmtvjD`

**Committing Changes:**
```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add feature: description"

# Push to branch (with retry logic for network failures)
git push -u origin claude/claude-md-mhyga4mpr1ck7iv4-01JMA64pL1haXBAmc1kmtvjD
```

**Branch Naming Convention:**
- Must start with `claude/`
- Must end with matching session ID
- Example: `claude/claude-md-mhyga4mpr1ck7iv4-01JMA64pL1haXBAmc1kmtvjD`

---

## Code Conventions

### Python Style

**Follow PEP 8:**
- 4 spaces for indentation
- Max line length: 79-100 characters
- Class names: `PascalCase`
- Function names: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

**Model Conventions:**
```python
class MyModel(models.Model):
    """Model docstring describing purpose"""

    # Fields in logical order:
    # 1. Core identifying fields (title, name, slug)
    # 2. Content fields
    # 3. Metadata fields
    # 4. Display/visibility toggles
    # 5. Timestamps

    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

**View Conventions:**
```python
def my_view(request):
    """View docstring describing purpose"""

    # 1. Get queryset/data
    items = MyModel.objects.filter(is_active=True)

    # 2. Build context
    context = {
        'items': items,
        'page_title': 'My Page'
    }

    # 3. Render template
    return render(request, 'my_page.html', context)
```

---

### Template Conventions

**Always extend base:**
```django
{% extends 'base.html' %}
{% load static %}
```

**Use semantic HTML:**
- `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`
- Proper heading hierarchy (h1 → h2 → h3)
- Descriptive alt text for images

**Tailwind Class Organization:**
```html
<!-- Group by: layout → spacing → sizing → colors → typography → effects -->
<div class="flex items-center gap-4 px-6 py-4 bg-neutral-100 text-neutral-900 rounded-lg shadow-sm hover:shadow-md transition-shadow">
```

**Template Comments:**
```django
{# Describe what this section does #}
<section>
  {# Loop through items #}
  {% for item in items %}
    {{ item.title }}
  {% endfor %}
</section>
```

---

### CSS Conventions

**Prefer Tailwind utilities over custom CSS**

**When creating custom components:**
```css
@layer components {
  .my-component {
    @apply flex items-center gap-4;
    @apply px-6 py-4;
    @apply bg-neutral-100 rounded-lg;
  }
}
```

**Custom utilities for repeated patterns:**
```css
@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}
```

---

### JavaScript Conventions

**Alpine.js State Management:**
```javascript
// Component-scoped state
x-data="{
  open: false,
  selected: null
}"

// Not global state on <body>
```

**Event Handling:**
```javascript
// Use shorthand
@click="open = !open"

// Not verbose
x-on:click="open = !open"
```

**Keep JavaScript minimal:**
- Use Alpine for simple interactivity
- No complex state management needed
- Progressive enhancement mindset

---

## Common Tasks

### Adding a Blog Post

**Via Django Admin:**
1. Navigate to http://localhost:8000/admin
2. Click "Articles" → "Add Article"
3. Fill in required fields:
   - Title (slug auto-generates)
   - Excerpt
   - Content
   - Article type
   - Read time
4. Optional: Add featured image, tags, custom CSS/JS
5. Set status to "Published"
6. Set published_at to current datetime
7. Click "Save"

**Programmatically:**
```python
from core.models import Article
from django.utils import timezone

article = Article.objects.create(
    title="My New Post",
    excerpt="Short summary of the post",
    content="Full content of the post...",
    article_type="essay",
    status="published",
    read_time=5,
    published_at=timezone.now()
)
```

---

### Adding Work Experience

**Via Django Admin:**
1. Go to "Experiences" → "Add Experience"
2. Select type: "Work"
3. Fill in:
   - Title (e.g., "Senior Product Manager")
   - Organization (e.g., "Company Name")
   - Location (e.g., "Nairobi, Kenya")
   - Start date and End date (leave blank if current)
   - Description
   - Achievements (JSON list: `["Achievement 1", "Achievement 2"]`)
   - Tech stack (JSON list: `["Python", "Django", "React"]`)
4. Set `is_visible = True`
5. Save

---

### Updating Resume

**Upload New Resume PDF:**
1. Go to "Resumes" → "Add Resume"
2. Upload PDF file
3. Add summary (optional)
4. Check "Is active" (automatically deactivates other resumes)
5. Save

**Note:** Only one resume can be active at a time (enforced by model)

---

### Managing Newsletter Subscribers

**View Subscribers:**
1. Admin → "Newsletter Subscribers"
2. See list with email, subscription date, status

**Export Subscribers (via Django shell):**
```python
python manage.py shell

from core.models import NewsletterSubscriber
subscribers = NewsletterSubscriber.objects.filter(is_active=True)
emails = [s.email for s in subscribers]
print('\n'.join(emails))
```

---

### Customizing Homepage "Now" Section

**Add/Edit Now Items:**
1. Admin → "Now Items" → "Add Now Item"
2. Fill in:
   - Title (e.g., "Writing a book")
   - Icon (emoji, e.g., "📚")
   - Description (what you're working on)
   - Link (optional)
   - Order (controls display sequence)
3. Set `is_active = True`
4. Save

**Items display on homepage in order**

---

### Adding Gallery Items

1. Admin → "Gallery Items" → "Add Gallery Item"
2. Upload image
3. Optionally upload separate thumbnail (or auto-generate)
4. Select item type (photo, design, art, project, other)
5. Add tags as JSON list: `["nature", "photography", "landscape"]`
6. Add external link if applicable
7. Set order and save

---

### Modifying Navigation Links

**Edit:** `/home/user/kenruto-portfolio/templates/components/nav.html`

**Add new link:**
```django
<a href="{% url 'my_page' %}"
   :class="currentPath === '/my-page/' ? 'text-accent-600 font-medium' : 'text-neutral-600 hover:text-neutral-900'"
   class="transition-colors">
   My Page
</a>
```

**Mobile menu:** Add same link in mobile menu section

---

### Creating a New Model

1. **Define model in `core/models.py`:**
   ```python
   class MyModel(models.Model):
       title = models.CharField(max_length=200)
       created_at = models.DateTimeField(auto_now_add=True)

       class Meta:
           ordering = ['-created_at']

       def __str__(self):
           return self.title
   ```

2. **Create and apply migration:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Register in admin (`core/admin.py`):**
   ```python
   from .models import MyModel

   @admin.register(MyModel)
   class MyModelAdmin(admin.ModelAdmin):
       list_display = ['title', 'created_at']
       search_fields = ['title']
   ```

4. **Create view, template, URL as needed**

---

## Production Considerations

### Critical Issues Before Deployment

**1. Environment Variables**

Currently hardcoded in `portfolio/settings.py`:
```python
SECRET_KEY = 'django-insecure-your-temporary-secret-key-here-change-later'
DEBUG = True
```

**Must create `.env` file:**
```bash
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=<production-database-url>
```

**Update `settings.py` to read from environment:**
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
```

---

**2. Dependencies Management**

**Create `requirements.txt`:**
```bash
pip freeze > requirements.txt
```

**Should include at minimum:**
```
Django>=5.2.7
whitenoise>=6.0.0
python-decouple  # For environment variables
gunicorn  # WSGI server
psycopg2-binary  # If using PostgreSQL
pillow  # For ImageField support
```

---

**3. Database Migration**

**Switch from SQLite to PostgreSQL:**

```python
# settings.py
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600
    )
}
```

**Migration steps:**
1. Set up PostgreSQL database
2. Update `DATABASE_URL` in environment
3. Run `python manage.py migrate`
4. Transfer data from SQLite if needed

---

**4. Static Files**

**Already configured with WhiteNoise, but verify:**

```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

**Before deployment:**
```bash
npm run build  # Compile Tailwind CSS
python manage.py collectstatic --noinput
```

---

**5. Media Files**

**Current:** Stored locally in `media/` directory

**Production options:**
- AWS S3 (recommended)
- Cloudinary
- DigitalOcean Spaces
- Google Cloud Storage

**Install `django-storages` for S3:**
```bash
pip install django-storages boto3
```

---

**6. Security Settings**

**Update `settings.py` for production:**

```python
# Security
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

---

**7. Email Configuration**

**Current:** Console backend (development only)

**Production options:**

```python
# Gmail SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Or use SendGrid, Mailgun, AWS SES
```

---

**8. Deployment Platform**

**Recommended platforms:**

1. **Heroku:**
   - Create `Procfile`:
     ```
     web: gunicorn portfolio.wsgi
     ```
   - Create `runtime.txt`:
     ```
     python-3.11.0
     ```

2. **DigitalOcean App Platform**
3. **Railway**
4. **Fly.io**
5. **AWS Elastic Beanstalk**

---

**9. Logging**

**Add production logging:**

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

---

**10. Monitoring**

**Recommended tools:**
- **Sentry** - Error tracking
- **New Relic** - Performance monitoring
- **Google Analytics** - User analytics
- **Uptime Robot** - Uptime monitoring

---

### Deployment Checklist

- [ ] Create `.env` file with production values
- [ ] Generate new `SECRET_KEY`
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure media file storage (S3/Cloudinary)
- [ ] Set up email backend (SMTP/SendGrid)
- [ ] Run `python manage.py check --deploy`
- [ ] Run `npm run build`
- [ ] Run `python manage.py collectstatic`
- [ ] Create `requirements.txt`
- [ ] Set up SSL certificate
- [ ] Configure security headers
- [ ] Set up error logging
- [ ] Set up monitoring (Sentry)
- [ ] Create database backups strategy
- [ ] Test all functionality on staging

---

## Important Files Reference

### Configuration Files

| File | Purpose | Notes |
|------|---------|-------|
| `portfolio/settings.py` | Django settings | Contains hardcoded SECRET_KEY (change for production) |
| `portfolio/urls.py` | Root URL configuration | Includes core.urls and admin |
| `tailwind.config.js` | Tailwind configuration | Custom colors, fonts, max-widths |
| `package.json` | Node dependencies | Tailwind build scripts |
| `.gitignore` | Git ignore rules | Excludes db, media, output.css, etc. |

### Core Application Files

| File | Lines | Purpose |
|------|-------|---------|
| `core/models.py` | 326 | 7 database models |
| `core/views.py` | 175 | 8 view functions |
| `core/admin.py` | 302 | Customized admin interface |
| `core/urls.py` | 23 | App URL routing |
| `core/forms.py` | 13 | Django forms (minimal) |

### Template Files

| File | Lines | Purpose |
|------|-------|---------|
| `templates/base.html` | ~100 | Base layout template |
| `templates/components/nav.html` | 186 | Navigation component |
| `templates/components/footer.html` | 80 | Footer component |
| `templates/components/newsletter.html` | 159 | Newsletter form |
| `templates/home.html` | - | Homepage |
| `templates/about.html` | - | About page |
| `templates/resume.html` | - | Resume page |
| `templates/kiota.html` | - | Essays listing |
| `templates/article_detail.html` | - | Article detail |
| `templates/gallery.html` | - | Gallery page |

### Static Files

| File | Lines | Purpose |
|------|-------|---------|
| `static/css/input.css` | 193 | Tailwind source CSS |
| `static/css/output.css` | - | Compiled CSS (gitignored) |
| `static/js/app.js` | 194 | Custom JavaScript + Alpine.js docs |

---

## URL Structure

```
/                          → home           → templates/home.html
/about/                    → about          → templates/about.html
/resume/                   → resume         → templates/resume.html
/essays/                   → kiota          → templates/kiota.html
/essays/<slug>/            → article_detail → templates/article_detail.html
/projects/                 → small_bets     → templates/small_bets.html
/gallery/                  → gallery        → templates/gallery.html
/tlw/                      → tlw_studio     → templates/tlw.html
/newsletter/subscribe/     → POST only      → newsletter_subscribe view
/admin/                    → Django Admin   → Customized interface
```

---

## Timezone & Localization

- **TIME_ZONE:** `'Africa/Nairobi'`
- **LANGUAGE_CODE:** `'en-us'`
- **USE_I18N:** `True`
- **USE_TZ:** `True` (timezone-aware datetimes)

---

## Quick Reference Commands

### Development
```bash
# Start Tailwind watch mode
npm run dev

# Start Django server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell
```

### Production
```bash
# Build CSS for production
npm run build

# Collect static files
python manage.py collectstatic --noinput

# Run deployment checks
python manage.py check --deploy

# Create requirements file
pip freeze > requirements.txt
```

### Git
```bash
# Stage changes
git add .

# Commit
git commit -m "Descriptive message"

# Push to current branch
git push -u origin claude/claude-md-mhyga4mpr1ck7iv4-01JMA64pL1haXBAmc1kmtvjD
```

---

## Tips for AI Assistants

### When Making Changes

1. **Always read files before editing**
   - Use Read tool to view current state
   - Understand context before modifications

2. **Update related files together**
   - Model change → migration → admin → view → template → URL
   - Keep everything in sync

3. **Follow existing patterns**
   - Match code style of existing files
   - Use established naming conventions
   - Maintain consistent structure

4. **Test changes locally**
   - Verify in browser
   - Check admin interface
   - Test responsive design
   - Validate forms

5. **Document your changes**
   - Add comments for complex logic
   - Update this CLAUDE.md if architecture changes
   - Write descriptive commit messages

### Common Pitfalls to Avoid

1. **Don't skip migrations**
   - Always run makemigrations after model changes
   - Apply migrations before testing

2. **Don't hardcode values**
   - Use Django settings for configuration
   - Use environment variables for secrets

3. **Don't break existing functionality**
   - Test all related pages after changes
   - Check admin interface still works

4. **Don't forget CSRF tokens**
   - All POST forms need `{% csrf_token %}`

5. **Don't ignore static file compilation**
   - Run `npm run build` before deployment
   - Ensure output.css is generated

### Helpful Debugging

**Django errors:**
- Read full traceback
- Check terminal output
- Look for migration issues
- Verify imports

**Tailwind not updating:**
- Is `npm run dev` running?
- Check `tailwind.config.js` content paths
- Verify input.css imports

**Alpine.js not working:**
- Check browser console for errors
- Verify Alpine.js CDN loaded
- Check syntax of x-data, @click, etc.

**Database issues:**
- Run migrations
- Check model field definitions
- Verify foreign key relationships

---

## Contact & Resources

### Project Maintainer
**Ken Ruto**
- GitHub: github.com/kkruto
- LinkedIn: linkedin.com/in/kennyruto
- Twitter: @KenRuto

### Documentation Links
- Django: https://docs.djangoproject.com/
- Tailwind CSS: https://tailwindcss.com/docs
- Alpine.js: https://alpinejs.dev/

### Project Repository
- Location: `/home/user/kenruto-portfolio`
- Current Branch: `claude/claude-md-mhyga4mpr1ck7iv4-01JMA64pL1haXBAmc1kmtvjD`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| MVP V 0.1 | 2025-11 | Initial portfolio launch with core features |

---

**Last Updated:** 2025-11-14
**Document Version:** 1.0.0
**For Questions:** Refer to inline code documentation or contact project maintainer
