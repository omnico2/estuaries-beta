from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly
from .models import Listing, ListingImage
from .serializers import ListingSerializer
from django.shortcuts import render, get_object_or_404


class ListingListView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


def listingimage_view(request):
    listing = Listing.objects.all()
    return render(request, 'listingimage.html', {'listing':listing})
 
def listingimagedetail_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    images = ListingImage.objects.filter(listing=listing)
    return render(request, 'listingimagedetail.html', {
        'listing':listing,
        'images':images
    })