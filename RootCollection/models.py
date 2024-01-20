from django.db import models


class Root(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.root} - {self.name}"


class AnimalKind(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category} - {self.name}"


class Animal(models.Model):
    kind = models.ForeignKey(AnimalKind, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.kind} - {self.name}"
