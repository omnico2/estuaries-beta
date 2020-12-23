from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Theme, Categories
from .serializers import ThemeSerializer, CategoriesSerializer
from .permissions import IsAdminOrReadOnly

class CategoriesListView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
class CategoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_field = 'slug'

def get_redirected(queryset_or_class, lookups, validators):
    obj = get_object_or_404(queryset_or_class, **lookups)
    return obj, None

def my_view(request, slug, id):
    categories, categories_url = get_redirected(Categories, {'pk': id}, {'slug': slug})
    if categories_url:
        return redirect(categories_url)

class ThemeListView(ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = (IsAdminOrReadOnly, )
