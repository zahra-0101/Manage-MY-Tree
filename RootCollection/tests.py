from django.test import TestCase
from .models import Root, Category, AnimalKind, Animal


class AnimalHierarchyTest(TestCase):
    def setUp(self):
        # Create test data for Root
        self.root = Root.objects.create(name='Test Root')

        # Create test data for Category
        self.category = Category.objects.create(
            root=self.root, name='Test Category')

        # Create test data for AnimalKind
        self.animal_kind = AnimalKind.objects.create(
            category=self.category, name='Test Animal Kind')

        # Create test data for Animal
        self.animal = Animal.objects.create(
            kind=self.animal_kind, name='Test Animal')

    def test_root_str(self):
        self.assertEqual(str(self.root), 'Test Root')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Root - Test Category')

    def test_animal_kind_str(self):
        self.assertEqual(str(self.animal_kind),
                         'Test Root - Test Category - Test Animal Kind')

    def test_animal_str(self):
        self.assertEqual(
            str(self.animal), 'Test Root - Test Category - Test Animal Kind - Test Animal')
