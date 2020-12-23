from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly
from .models import Listing
from .serializers import ListingSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ListingListView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    paginate_by = 10
    ordering = ["-created_at"]

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'