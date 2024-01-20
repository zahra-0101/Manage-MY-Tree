from django.urls import path
from .views import tree_view

urlpatterns = [
    path('tree/', tree_view, name='tree_view'),
]
