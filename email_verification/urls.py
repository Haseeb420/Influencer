from django.urls import path, include
from email_verification.views import index, SearchEmail


urlpatterns = [
    path('', index),
    path('search-email', SearchEmail, name="search-email"),
]
