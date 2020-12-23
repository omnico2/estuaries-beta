from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from users.views import GoogleLogin, UserDetailView


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
	path('user/<slug:slug>/', UserDetailView.as_view())
]
