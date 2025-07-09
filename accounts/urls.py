"""Define URL patterns for accounts."""

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),  # Django内置了认证的URL
    # Registration page.
    path('register/', views.register, name='register')

]
