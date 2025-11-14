"""
Custom template tags for markdown rendering
"""
from django import template
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(text):
    """
    Converts markdown text to HTML

    Usage in templates:
        {{ article.content|markdown }}

    Supports:
    - Headers (# ## ###)
    - Bold (**text**)
    - Italic (*text*)
    - Links [text](url)
    - Images ![alt](url)
    - Code blocks ```code```
    - Lists (- item)
    - Blockquotes (> quote)
    """
    if not text:
        return ''

    # Markdown extras for better formatting
    extras = [
        'fenced-code-blocks',  # ```python code ```
        'tables',              # GitHub-style tables
        'code-friendly',       # Better handling of underscores
        'break-on-newline',    # Convert \n to <br>
        'cuddled-lists',       # Better list handling
        'header-ids',          # Add IDs to headers for linking
        'footnotes',           # [^1] footnote syntax
        'strike',              # ~~strikethrough~~
        'task_list',           # - [ ] task items
    ]

    html = markdown2.markdown(text, extras=extras)
    return mark_safe(html)
