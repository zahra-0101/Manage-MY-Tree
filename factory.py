import os
from faker import Faker
from django.core.wsgi import get_wsgi_application

from django.conf import settings

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manageMyTree.settings')
django.setup()


from RootCollection.models import Root, Category, AnimalKind, Animal

fake = Faker()


def create_data(n):
    for _ in range(n):
        root_name = fake.word()
        root = Root.objects.create(name=root_name)

        for _ in range(n):
            category_name = fake.word()
            category = Category.objects.create(name=category_name, root=root)

            for _ in range(n):
                kind_name = fake.word()
                kind = AnimalKind.objects.create(
                    name=kind_name, category=category)

                for _ in range(n):
                    animal_name = fake.name()
                    Animal.objects.create(name=animal_name, kind=kind)


if __name__ == "__main__":
    print("Populating the database with fake data...")
    create_data(5)  # Adjust the number as needed
    print("Populating complete.")
