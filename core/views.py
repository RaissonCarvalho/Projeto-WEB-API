from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from core.serializers import *
from core.models import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-details'
    lookup_field = 'pk'


class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-details'


class ApiRoot(generics.GenericAPIView):
    name = 'API'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'documentation': reverse('documentation', request=request),
                'users': reverse(UserList.name, request=request),
                'profiles': reverse(ProfilesList.name, request=request),
            }
        )