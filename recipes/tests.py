from django.test import TestCase
from django.urls import reverse


class RecipeViewTests(TestCase):
    def test_homepage_renders_recipe_links(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse('recipes:recipe', args=[1]))

    def test_recipe_detail_renders(self):
        response = self.client.get(reverse('recipes:recipe', args=[1]))

        self.assertEqual(response.status_code, 200)
