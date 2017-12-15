from rest_framework import routers, serializers, viewsets
from profile.models import UserProfile

class UserProfileSerializator(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user', 'website', 'phone', 'city', 'country', 'organization')