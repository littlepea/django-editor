from django.db import models
from django.contrib import admin
from django.forms.widgets import Textarea
from django.conf import settings

rich_text_module = None

if 'imperavi' in settings.INSTALLED_APPS:
    try:
        # use django-imperavi if installed
        from imperavi.admin import ImperaviAdmin, \
            ImperaviStackedInlineAdmin, \
            ImperaviWidget
        rich_text_module = "imperavi"
    except ImportError:
        rich_text_module = None

if not rich_text_module and 'tinymce' in settings.INSTALLED_APPS:
    try:
        # fallback to django-tinymce
        from tinymce.widgets import TinyMCE
        rich_text_module = "tinymce"
    except ImportError:
        # or use  default editor
        rich_text_module = None

if rich_text_module == "imperavi":
    # take all three admin classes from imperavi
    StackedInline = ImperaviStackedInlineAdmin
    Admin = ImperaviAdmin
    Widget = ImperaviWidget
else:
    # fallback to default
    StackedInline = admin.StackedInline
    Admin = admin.ModelAdmin
    if rich_text_module == "tinymce":
        # take only widget from tinymce
        Widget = TinyMCE
    else:
        # or use default widget
        Widget = Textarea


class EditorAdmin(Admin):
    """
    Universal Admin class for pluggable editor
    """
    if rich_text_module == "tinymce":
        formfield_overrides = {
            models.TextField: {'widget': Widget},
        }


class EditorStackedInline(StackedInline):
    """
    Universal StackedInline class for pluggable editor
    """
    if rich_text_module == "tinymce":
        formfield_overrides = {
            models.TextField: {'widget': Widget},
        }


class EditorWidget(Widget):
    """
    Universal TextField Widget class for pluggable editor
    """
    class Media:
        if rich_text_module == "imperavi":
            js = (
                '%simperavi/jquery.js' % settings.STATIC_URL,
                '%simperavi/redactor/redactor.min.js' % settings.STATIC_URL,
            )
            css = {
                'all': (
                    "%simperavi/redactor/css/redactor.css" %
                    settings.STATIC_URL,
                ),
            }
        else:
            pass
