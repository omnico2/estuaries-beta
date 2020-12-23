from django.urls import path, include
from .views import ListingListView, ListingDetailView
from django.urls import path
from listings import views
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r'', ListingViewSet)

urlpatterns = [
    path('listings/', ListingListView.as_view()),
	path('listings/<slug:slug>/', ListingDetailView.as_view())
]
