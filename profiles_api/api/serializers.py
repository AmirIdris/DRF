from rest_framework import serializers

from profiles_api.models import Profile,ProfileStatus

class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    avatar=serializers.ImageField(read_only=True)

    class Meta:
        model=Profile
        fields="__all__"

class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields=("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile=user=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=ProfileStatus
        fields="__all__"
