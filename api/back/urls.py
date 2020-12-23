from django.urls import path
from .views import ThemeListView, CategoriesDetailView, CategoriesListView
from django.urls import path

urlpatterns = [
    path('themelist/', ThemeListView.as_view()),
    path('categorieslist/', CategoriesListView.as_view()),
	path('categories/<slug:slug>/', CategoriesDetailView.as_view())
]
