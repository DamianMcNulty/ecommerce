from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig


class TestCartConfig(TestCase):

    def test_app(self):
        self.assertEqual("cart", TodoConfig.name)
        self.assertEqual("cart", apps.get_app_config("todo").name)