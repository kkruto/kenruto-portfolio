"""
Management command to populate database with realistic dummy data

Usage: python manage.py populate_dummy_data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from core.models import (
    NewsletterSubscriber,
    Experience,
    NowItem,
    Skill,
    Article,
    GalleryItem,
    Resume
)


class Command(BaseCommand):
    help = 'Populates database with realistic dummy data for Ken Ruto portfolio'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('\n🚀 Starting dummy data population...\n'))

        # Clear existing data (optional - comment out if you want to keep existing data)
        self.stdout.write('Clearing existing data...')
        Article.objects.all().delete()
        Experience.objects.all().delete()
        NowItem.objects.all().delete()
        Skill.objects.all().delete()
        GalleryItem.objects.all().delete()
        # Don't delete Resume objects to avoid issues

        # Create data
        self.create_now_items()
        self.create_skills()
        self.create_experiences()
        self.create_articles()
        self.create_newsletter_subscribers()

        self.stdout.write(self.style.SUCCESS('\n✅ Dummy data population complete!\n'))
        self.stdout.write(self.style.SUCCESS('📊 Summary:'))
        self.stdout.write(f'  - Articles: {Article.objects.count()}')
        self.stdout.write(f'  - Projects: {Experience.objects.filter(type="project").count()}')
        self.stdout.write(f'  - Work Experience: {Experience.objects.filter(type="work").count()}')
        self.stdout.write(f'  - Skills: {Skill.objects.count()}')
        self.stdout.write(f'  - Now Items: {NowItem.objects.count()}')
        self.stdout.write(f'  - Newsletter Subscribers: {NewsletterSubscriber.objects.count()}\n')

    def create_now_items(self):
        """Create 'What I'm Doing Now' items"""
        self.stdout.write('Creating Now items...')

        now_items = [
            {
                'title': 'Building AI-powered tools',
                'icon': '🤖',
                'description': 'Exploring how AI can make product management more efficient. Currently experimenting with GPT-4 for user research analysis.',
                'link': '',
                'order': 1
            },
            {
                'title': 'Writing about product strategy',
                'icon': '✍️',
                'description': 'Publishing weekly essays on product thinking, strategy frameworks, and lessons learned from building products.',
                'link': '/essays/',
                'order': 2
            },
            {
                'title': 'Traveling through East Africa',
                'icon': '🌍',
                'description': 'Documenting my journey through Kenya, Tanzania, and Uganda. Capturing stories and landscapes along the way.',
                'link': '/gallery/',
                'order': 3
            }
        ]

        for item_data in now_items:
            NowItem.objects.create(**item_data)
            self.stdout.write(f'  ✓ Created: {item_data["title"]}')

    def create_skills(self):
        """Create skills by category"""
        self.stdout.write('\nCreating skills...')

        skills = [
            # Product Management
            {'category': 'product', 'name': 'Product Strategy', 'order': 1},
            {'category': 'product', 'name': 'User Research', 'order': 2},
            {'category': 'product', 'name': 'Roadmap Planning', 'order': 3},
            {'category': 'product', 'name': 'Data Analysis', 'order': 4},
            {'category': 'product', 'name': 'A/B Testing', 'order': 5},
            {'category': 'product', 'name': 'Agile/Scrum', 'order': 6},

            # Engineering
            {'category': 'engineering', 'name': 'Python', 'order': 1},
            {'category': 'engineering', 'name': 'Django', 'order': 2},
            {'category': 'engineering', 'name': 'React', 'order': 3},
            {'category': 'engineering', 'name': 'JavaScript', 'order': 4},
            {'category': 'engineering', 'name': 'SQL/PostgreSQL', 'order': 5},
            {'category': 'engineering', 'name': 'Git', 'order': 6},
            {'category': 'engineering', 'name': 'REST APIs', 'order': 7},
            {'category': 'engineering', 'name': 'AWS', 'order': 8},

            # Leadership
            {'category': 'leadership', 'name': 'Team Building', 'order': 1},
            {'category': 'leadership', 'name': 'Stakeholder Management', 'order': 2},
            {'category': 'leadership', 'name': 'Strategic Planning', 'order': 3},
            {'category': 'leadership', 'name': 'Mentoring', 'order': 4},

            # Design
            {'category': 'design', 'name': 'Figma', 'order': 1},
            {'category': 'design', 'name': 'User Experience', 'order': 2},
            {'category': 'design', 'name': 'Wireframing', 'order': 3},
            {'category': 'design', 'name': 'Design Systems', 'order': 4},
        ]

        for skill_data in skills:
            Skill.objects.create(**skill_data)

        self.stdout.write(f'  ✓ Created {len(skills)} skills')

    def create_experiences(self):
        """Create work experience, education, and projects"""
        self.stdout.write('\nCreating experiences...')

        # Work Experience
        work_experiences = [
            {
                'type': 'work',
                'title': 'Senior Product Manager',
                'organization': 'TechCorp Africa',
                'location': 'Nairobi, Kenya',
                'start_date': datetime(2022, 3, 1).date(),
                'end_date': None,  # Current position
                'description': 'Leading product development for B2B SaaS platform serving 500+ African businesses. Responsible for product strategy, roadmap, and cross-functional team leadership.',
                'achievements': [
                    'Grew user base from 200 to 500+ businesses (150% growth)',
                    'Reduced churn by 40% through improved onboarding experience',
                    'Launched 3 major features that increased MRR by $50k',
                    'Built and mentored team of 2 associate product managers'
                ],
                'tech_stack': ['Python', 'Django', 'React', 'PostgreSQL', 'AWS'],
                'order': 1
            },
            {
                'type': 'work',
                'title': 'Product Manager',
                'organization': 'FinTech Innovations',
                'location': 'Remote',
                'start_date': datetime(2020, 6, 1).date(),
                'end_date': datetime(2022, 2, 28).date(),
                'description': 'Led mobile payments product serving 100k+ users across East Africa. Managed full product lifecycle from ideation to launch.',
                'achievements': [
                    'Launched MVP in 4 months with 10k users in first month',
                    'Achieved 4.8/5 app store rating',
                    'Reduced transaction failure rate from 8% to 2%',
                    'Led integration with 5 major payment providers'
                ],
                'tech_stack': ['React Native', 'Node.js', 'MongoDB', 'AWS'],
                'order': 2
            },
            {
                'type': 'work',
                'title': 'Software Engineer',
                'organization': 'StartupXYZ',
                'location': 'Nairobi, Kenya',
                'start_date': datetime(2018, 1, 1).date(),
                'end_date': datetime(2020, 5, 31).date(),
                'description': 'Full-stack engineer building web applications. Transitioned to product management role after 2 years.',
                'achievements': [
                    'Built core features serving 50k+ daily active users',
                    'Reduced page load time by 60% through optimization',
                    'Mentored 3 junior engineers',
                    'Led migration from monolith to microservices'
                ],
                'tech_stack': ['Python', 'Django', 'Vue.js', 'PostgreSQL', 'Docker'],
                'order': 3
            }
        ]

        for exp_data in work_experiences:
            Experience.objects.create(**exp_data)
            self.stdout.write(f'  ✓ Work: {exp_data["title"]} at {exp_data["organization"]}')

        # Education
        education = [
            {
                'type': 'education',
                'title': 'BSc Computer Science',
                'organization': 'University of Nairobi',
                'location': 'Nairobi, Kenya',
                'start_date': datetime(2014, 9, 1).date(),
                'end_date': datetime(2018, 6, 30).date(),
                'description': 'Focused on software engineering, algorithms, and human-computer interaction. Graduated with First Class Honours.',
                'achievements': [
                    'First Class Honours (GPA: 3.8/4.0)',
                    'President of Computer Science Society',
                    'Winner of National Hackathon 2017',
                    'Research paper published on mobile UX'
                ],
                'tech_stack': [],
                'order': 1
            }
        ]

        for edu_data in education:
            Experience.objects.create(**edu_data)
            self.stdout.write(f'  ✓ Education: {edu_data["title"]}')

        # Projects
        projects = [
            {
                'type': 'project',
                'title': 'TaskFlow - AI Task Manager',
                'organization': 'Side Project',
                'location': 'Remote',
                'start_date': datetime(2024, 1, 1).date(),
                'end_date': None,  # Active project
                'description': '''An intelligent task management app that uses AI to help you prioritize your work.

Built with modern web technologies and GPT-4 API for smart task suggestions.

## Features
- AI-powered task prioritization
- Natural language task input
- Smart deadline suggestions
- Integration with Google Calendar
- Beautiful, minimal interface

## Technical Highlights
- Built in 3 weeks
- 200+ beta users
- 4.7/5 user satisfaction score''',
                'achievements': [
                    'Reached 200+ beta users in first month',
                    'Featured in "Indie Hackers" newsletter',
                    'Built entire MVP in 3 weeks',
                    'Positive user feedback: 4.7/5 average rating'
                ],
                'tech_stack': ['Django', 'Python', 'React', 'Tailwind CSS', 'OpenAI API', 'PostgreSQL'],
                'link': 'https://github.com/kenruto/taskflow',
                'order': 1
            },
            {
                'type': 'project',
                'title': 'AfriMarket Analytics',
                'organization': 'Freelance',
                'location': 'Remote',
                'start_date': datetime(2023, 6, 1).date(),
                'end_date': datetime(2023, 12, 31).date(),
                'description': 'Analytics dashboard for African e-commerce businesses. Provides insights on sales, inventory, and customer behavior.',
                'achievements': [
                    'Served 50+ small businesses',
                    'Generated $5k in revenue',
                    'Built custom data pipeline processing 1M+ events/day',
                    'Helped clients increase sales by avg 25%'
                ],
                'tech_stack': ['Python', 'FastAPI', 'React', 'Chart.js', 'PostgreSQL', 'Redis'],
                'link': '',
                'order': 2
            },
            {
                'type': 'project',
                'title': 'HealthTrack Mobile App',
                'organization': 'Side Project',
                'location': 'Remote',
                'start_date': datetime(2022, 9, 1).date(),
                'end_date': datetime(2023, 3, 31).date(),
                'description': 'Mobile health tracking app for chronic disease management. Focused on simplicity and accessibility for non-tech-savvy users.',
                'achievements': [
                    'Downloaded by 1,000+ users',
                    'Won "Best Health App" at local startup competition',
                    'Partnered with 2 healthcare NGOs',
                    'Featured in TechCrunch article'
                ],
                'tech_stack': ['React Native', 'Firebase', 'Node.js', 'MongoDB'],
                'link': 'https://github.com/kenruto/healthtrack',
                'order': 3
            },
            {
                'type': 'project',
                'title': 'Portfolio Website Generator',
                'organization': 'Open Source',
                'location': 'Remote',
                'start_date': datetime(2021, 11, 1).date(),
                'end_date': datetime(2022, 2, 28).date(),
                'description': 'Open-source tool to help developers create beautiful portfolio websites with no coding required. Template-based with customization options.',
                'achievements': [
                    '500+ GitHub stars',
                    'Used by 200+ developers',
                    'Featured in "Awesome Python" list',
                    '15 community contributors'
                ],
                'tech_stack': ['Python', 'Django', 'Jinja2', 'Tailwind CSS'],
                'link': 'https://github.com/kenruto/portfolio-gen',
                'order': 4
            }
        ]

        for proj_data in projects:
            Experience.objects.create(**proj_data)
            self.stdout.write(f'  ✓ Project: {proj_data["title"]}')

    def create_articles(self):
        """Create blog articles including one with Chart.js visualization"""
        self.stdout.write('\nCreating articles...')

        articles = [
            {
                'title': 'The Product Manager\'s Guide to Data-Driven Decisions',
                'slug': 'pm-guide-data-driven-decisions',
                'excerpt': 'A practical framework for making better product decisions using data. Learn how to balance quantitative metrics with qualitative insights.',
                'content': '''# The Product Manager's Guide to Data-Driven Decisions

As product managers, we're constantly making decisions. Which feature to build next? How to prioritize the roadmap? What metrics should we track?

The answer often lies in data, but knowing *how* to use data effectively is the real challenge.

## The Data-Driven Framework

I've developed a simple framework that helps me make better decisions:

1. **Define the question clearly**
2. **Identify relevant metrics**
3. **Collect qualitative context**
4. **Make the decision**
5. **Measure the outcome**

### 1. Define the Question

Before diving into data, be crystal clear about what you're trying to decide. Vague questions lead to confusion.

**Bad**: "Should we improve the onboarding?"
**Good**: "Should we add a product tour to reduce day-1 churn?"

### 2. Identify Relevant Metrics

Choose 2-3 key metrics that directly relate to your question. More isn't always better.

For the onboarding question, relevant metrics might be:
- Day-1 activation rate
- Time to first value
- Day-7 retention

### 3. Collect Qualitative Context

Numbers tell you *what* is happening. User research tells you *why*.

Talk to users. Watch session recordings. Read support tickets. This context is crucial for interpreting the data correctly.

### 4. Make the Decision

Combine your quantitative data and qualitative insights. Trust your judgment, but let data inform it.

Remember: **Data informs decisions, it doesn't make them.**

### 5. Measure the Outcome

After implementing your decision, track the impact. This creates a feedback loop that improves your decision-making over time.

## Common Pitfalls

**Vanity Metrics**: Focus on metrics that drive real business outcomes, not just impressive-looking numbers.

**Analysis Paralysis**: Don't wait for perfect data. Make decisions with the information you have.

**Confirmation Bias**: Actively look for data that challenges your assumptions.

## Conclusion

Data-driven decision making is a skill that improves with practice. Start with this framework, adapt it to your context, and iterate.

The best product managers don't just look at data—they know which data to look at and why.''',
                'article_type': 'essay',
                'status': 'published',
                'read_time': 7,
                'published_date': timezone.now() - timedelta(days=5),
                'tags': ["product management, data analysis, decision making".split(', ')],
                'is_featured': True,
                'has_interactive_content': False,
            },
            {
                'title': 'Visualizing Product Metrics That Matter',
                'slug': 'visualizing-product-metrics',
                'excerpt': 'An interactive guide to the most important product metrics every PM should track. Includes real data visualizations and interpretation tips.',
                'content': '''# Visualizing Product Metrics That Matter

Understanding your product's health requires tracking the right metrics. But which metrics actually matter?

After years of product management, I've narrowed it down to 5 core categories.

## The 5 Essential Metric Categories

### 1. Acquisition Metrics
How users discover and sign up for your product.

### 2. Activation Metrics
How quickly users experience your product's value.

### 3. Engagement Metrics
How frequently users return and interact with your product.

### 4. Retention Metrics
How well you keep users over time.

### 5. Revenue Metrics
How your product drives business value.

## Example: SaaS Product Metrics

Below is an interactive chart showing typical SaaS metrics across a quarter:

<canvas id="metricsChart" width="400" height="200"></canvas>

## How to Interpret These Metrics

**MRR Growth**: Steady climb is ideal. Flat or declining MRR requires immediate attention.

**User Retention**: Aim for >40% at 30 days for consumer products, >70% for B2B.

**Churn Rate**: Keep below 5% monthly for B2B, 10% for consumer products.

## Taking Action

1. **Set benchmarks** for your industry
2. **Track trends** over time, not just absolute numbers
3. **Segment data** to find insights (e.g., power users vs. casual users)
4. **Correlate metrics** to understand relationships

## Conclusion

Metrics are your product's vital signs. Track them consistently, understand what they mean, and use them to guide your product decisions.

Remember: **The best metric is the one that drives action.**''',
                'article_type': 'data_essay',
                'status': 'published',
                'read_time': 10,
                'published_date': timezone.now() - timedelta(days=10),
                'tags': ["data visualization, product metrics, analytics".split(', ')],
                'is_featured': True,
                'has_interactive_content': True,
                'custom_css': '''
.chart-container {
    position: relative;
    margin: 2rem 0;
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 8px;
}
''',
                'custom_javascript': '''
// Chart.js visualization
const ctx = document.getElementById('metricsChart');
if (ctx) {
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [
                {
                    label: 'MRR ($k)',
                    data: [12, 15, 18, 22, 28, 35],
                    borderColor: '#2563eb',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    tension: 0.4
                },
                {
                    label: 'Active Users',
                    data: [450, 520, 680, 820, 950, 1100],
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    tension: 0.4
                },
                {
                    label: 'Churn Rate (%)',
                    data: [8.5, 7.2, 6.8, 5.5, 4.8, 4.2],
                    borderColor: '#ef4444',
                    backgroundColor: 'rgba(239, 68, 68, 0.1)',
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Key SaaS Metrics Over 6 Months'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
'''
            },
            {
                'title': 'Building Products for Africa: Lessons Learned',
                'slug': 'building-products-for-africa',
                'excerpt': 'What I\'ve learned building products for African markets. From infrastructure challenges to user behavior insights.',
                'content': '''# Building Products for Africa: Lessons Learned

Africa is not a monolith. But there are patterns I've observed building products across Kenya, Nigeria, Tanzania, and Uganda.

## Key Insights

### 1. Mobile-First is Not Enough
You need to be **mobile-only**. Desktop usage is minimal outside corporate environments.

### 2. Data Costs Matter
Users are acutely aware of data usage. Optimize aggressively:
- Compress images
- Minimize API calls
- Cache aggressively
- Consider offline-first architecture

### 3. Payment Infrastructure is Complex
Multiple payment methods are essential:
- Mobile money (M-Pesa, Airtel Money, etc.)
- Bank transfers
- Cash on delivery
- Card payments (but usage is low)

### 4. Trust is Everything
Users are skeptical of new platforms. Build trust through:
- Social proof (testimonials, user counts)
- Local partnerships
- Community engagement
- Excellent customer support

### 5. Localization Goes Beyond Language
- Use local examples and references
- Price in local currency
- Show prices that match local purchasing power
- Consider cultural nuances in design

## Biggest Mistakes I Made

**Assuming Western UX patterns work**: They often don't. Test everything with local users.

**Underestimating the importance of offline functionality**: Connectivity is unreliable.

**Ignoring feature phone users**: In some markets, smartphones aren't ubiquitous yet.

## What's Working

Products that:
- Solve real, urgent problems
- Work reliably with poor connectivity
- Are affordable (or free with clear value)
- Build community and trust
- Integrate with existing behaviors

## Conclusion

Building for African markets is challenging but incredibly rewarding. The potential is enormous for products that truly understand and serve users' needs.

Focus on solving real problems, not importing solutions from other markets.''',
                'article_type': 'essay',
                'status': 'published',
                'read_time': 8,
                'published_date': timezone.now() - timedelta(days=20),
                'tags': ["africa, product development, emerging markets".split(', ')],
                'is_featured': False,
            },
            {
                'title': 'My Product Management Reading List',
                'slug': 'pm-reading-list',
                'excerpt': 'Essential books, articles, and resources that shaped how I think about product management.',
                'content': '''# My Product Management Reading List

The resources that shaped my thinking as a product manager.

## Books

### Must-Reads

**Inspired** by Marty Cagan
The definitive guide to modern product management.

**The Mom Test** by Rob Fitzpatrick
How to talk to customers and learn if your idea is good—when everyone is lying to you.

**Hooked** by Nir Eyal
Understanding habit-forming products.

### Also Recommended

- **Continuous Discovery Habits** by Teresa Torres
- **Escaping the Build Trap** by Melissa Perri
- **Lean Analytics** by Alistair Croll & Benjamin Yoskovitz

## Blogs & Newsletters

- **Lenny's Newsletter** - Weekly PM insights
- **Stratechery** - Ben Thompson on tech strategy
- **Product Coalition** - Community-driven PM content

## Podcasts

1. **Lenny's Podcast** - Interviews with top PMs
2. **This is Product Management** - Practical PM advice
3. **Masters of Scale** - Reid Hoffman's startup wisdom

## Online Courses

- **Reforge** - Advanced product courses
- **Product School** - Fundamentals and certification
- **Coursera: Digital Product Management** - Academic foundation

## Communities

- **Mind the Product** - Global PM community
- **Product Hunt** - Discover new products
- **Indie Hackers** - Learn from indie founders

## My Learning Approach

**80/20 Rule**: Focus on resources that give you actionable insights, not just theory.

**Practice Over Theory**: Read less, build more. Apply what you learn immediately.

**Community Learning**: Join PM communities. The best insights come from conversations with other PMs.

## Conclusion

This list is constantly evolving. The best resource is your own experience—ship products, talk to users, and learn from your mistakes.

What's on your reading list? [Email me](mailto:kenruto@example.com) your recommendations.''',
                'article_type': 'tutorial',
                'status': 'published',
                'read_time': 5,
                'published_date': timezone.now() - timedelta(days=30),
                'tags': ["resources, learning, books, product management".split(', ')],
                'is_featured': False,
            }
        ]

        for article_data in articles:
            Article.objects.create(**article_data)
            self.stdout.write(f'  ✓ Article: {article_data["title"]}')

    def create_newsletter_subscribers(self):
        """Create sample newsletter subscribers"""
        self.stdout.write('\nCreating newsletter subscribers...')

        subscribers = [
            'jane.doe@example.com',
            'john.smith@example.com',
            'product.enthusiast@example.com',
        ]

        for email in subscribers:
            NewsletterSubscriber.objects.get_or_create(email=email)

        self.stdout.write(f'  ✓ Created {len(subscribers)} newsletter subscribers')
