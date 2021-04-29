from profiles_api.models import Profile
from profiles_api.api.serializers import UserProfileSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ListUserProfile(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated]
    