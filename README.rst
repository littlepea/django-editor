Django-editor
==========================

.. image:: https://travis-ci.org/littlepea/django-editor.png?branch=master
    :target: http://travis-ci.org/littlepea/django-editor

Allows pluggable WYSIWYG editors in django admin without hard dependencies.

Currently supported editors (both optional):

* `django-imperavi`_
* `django-tinycme`_

Installation
------------

1. Install with pip::

    pip install django-editor

2. (optional) Add `imperavi` or `tinymce` to your INSTALLED_APPS in `settings.py`::

    INSTALLED_APPS = (
        ...
        # Imperavi (or tinymce) rich text editor is optional
        'imperavi',
    )

Usage
-----

`editor` package gives you the following replacement classes:

* `django.forms.widgets.Textarea` => `editor.EditorWidget` (becomes `ImperaviWidget` or `TinyMCE`)
* `django.contrib.admin.ModelAdmin` => `editor.EditorAdmin` (becomes `ImperaviAdmin` or stays as `ModelAdmin`)
* `django.contrib.admin.StackedInline` => `editor.EditorStackedInline` (becomes `ImperaviStackedInline` or stays as `StackedInline`)

Here are some examples on how to easily turn your Textareas into WYSIWYG editors::

    # admin.py
    from django.db import models
    from django.contrib import admin
    from editor.admin import EditorAdmin, EditorWidget, EditorStackedInline


    class MyInlineAdmin(EditorStackedInline): # StackedInline example
        model = Model1


    class MyModel2Admin(EditorAdmin): # ModelAdmin example
        inlines = [MyInlineAdmin]

    admin.site.register(Model2, MyModel2Admin)


    class MyModel3Admin(admin.ModelAdmin):
        formfield_overrides = {
            models.TextField: {'widget': EditorWidget},
        }

    admin.site.register(Model3, MyModel3Admin)

Credits
-------

- `django-imperavi`_
- `django-tinycme`_
- `modern-package-template`_
- `django-newsletter`_ for providing pluggable editor code idea

.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template
.. _django-imperavi: https://github.com/vasyabigi/django-imperavi
.. _django-tinycme: https://github.com/aljosa/django-tinymce
.. _django-newsletter: https://github.com/dokterbob/django-newsletter
