from django.urls import path

from profiles_api.api import views

urlpatterns = [
    path('profiles/',views.ListUserProfile.as_view(),name="profile-list")
]