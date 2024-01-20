from django.shortcuts import render
from .models import Animal, AnimalKind, Category, Root
from django.db.models import Prefetch


def tree_view(request):
    roots = Root.objects.prefetch_related(
        Prefetch('category_set__animalkind_set__animal_set', queryset=Animal.objects.select_related('kind__category__root'))
    ).all()

    context = {}
    context['roots'] = roots
    return render(request, "dashboard.html", context)
