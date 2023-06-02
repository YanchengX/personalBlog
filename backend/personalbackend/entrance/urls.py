from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('sign-up/',views.SignupCreate.as_view()),
]
 