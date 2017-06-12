# -*- coding: utf-8 -*-
from django.test import TestCase
from django.template import loader, Context


class TemplateTagTests(TestCase):
    """Test Cases for template tags."""

    def setUp(self):
        """Setup test."""
        self.template = 'trello_webhooks/addAttachmentToCard.html'
        self.action_data_image = {
            'data': {
                'attachment': {
                    'url': 'http://www.example.com/',
                    'name': 'example',
                    'content_type': 'image/png'
                }
            }
        }
        self.action_data_zipfile = {
            'data': {
                'attachment': {
                    'url': 'http://www.example.com/',
                    'name': 'example',
                    'content_type': 'application/x-7z-compressed'
                }
            }
        }

    def test_successful_image_content_html_rendering(self):
        """Test html image tags render when content type is image."""
        t = loader.get_template(self.template)
        c = Context({'action': self.action_data_image})
        rendered = t.render(c)

        self.assertIn("attachment", rendered)
        self.assertIn("href", rendered)
        self.assertIn("<img src=", rendered)
        self.assertIn("www.example.com", rendered)

    def test_failed_image_content_html_rendering(self):
        """Test html image tags do not render when content type is zipfile."""
        t = loader.get_template(self.template)
        c = Context({'action': self.action_data_zipfile})
        rendered = t.render(c)

        self.assertIn("attachment", rendered)
        self.assertIn("href", rendered)
        self.assertNotIn("<img src=", rendered)
        self.assertIn("www.example.com", rendered)