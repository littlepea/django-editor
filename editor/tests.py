from django.test.utils import setup_test_environment, override_settings
setup_test_environment()

import imp

from django.utils import unittest
from django.conf import settings

from . import admin


class EditorTestBase(unittest.TestCase):
    def test_rich_text_module(self, expected=None):
        imp.reload(admin)
        module = admin.rich_text_module
        self.assertEquals(module, expected)

    def test_admin(self,
                   expected_widget=None,
                   expected_admin=None,
                   expected_inline=None):
        if not expected_widget:
            from django.forms.widgets import Textarea
            expected_widget = Textarea
        if not expected_admin or not expected_inline:
            from django.contrib.admin import ModelAdmin, StackedInline
            expected_admin = ModelAdmin
            expected_inline = StackedInline
        imp.reload(admin)
        self.assertEquals(admin.EditorWidget.__base__, expected_widget)
        self.assertEquals(admin.EditorAdmin.__base__, expected_admin)
        self.assertEquals(admin.EditorStackedInline.__base__, expected_inline)


class EditorTinyMCETest(EditorTestBase):
    @override_settings(INSTALLED_APPS=settings.INSTALLED_APPS+('tinymce',))
    def test_rich_text_module(self, **kwargs):
        super(EditorTinyMCETest, self).test_rich_text_module(
            expected='tinymce'
        )

    @override_settings(INSTALLED_APPS=settings.INSTALLED_APPS+('tinymce',))
    def test_admin(self, **kwargs):
        from tinymce.widgets import TinyMCE
        super(EditorTinyMCETest, self).test_admin(expected_widget=TinyMCE)


class EditorImperaviTest(EditorTestBase):
    @override_settings(INSTALLED_APPS=settings.INSTALLED_APPS+('imperavi',))
    def test_rich_text_module(self, **kwargs):
        super(EditorImperaviTest, self).test_rich_text_module(
            expected='imperavi'
        )

    @override_settings(INSTALLED_APPS=settings.INSTALLED_APPS+('imperavi',))
    def test_admin(self, **kwargs):
        from imperavi.admin import ImperaviAdmin, \
            ImperaviStackedInlineAdmin, \
            ImperaviWidget
        super(EditorImperaviTest, self).test_admin(
            expected_widget=ImperaviWidget,
            expected_admin=ImperaviAdmin,
            expected_inline=ImperaviStackedInlineAdmin
        )
