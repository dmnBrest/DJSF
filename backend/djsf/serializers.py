from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer): #serializers.HyperlinkedModelSerializer
    class Meta:
        model = User
        fields = ('url', 'password', 'username', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)