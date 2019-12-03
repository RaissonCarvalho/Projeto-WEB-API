from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from core.permissions import *
from core.serializers import *
from core.models import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (IsSuperUser,)


class UserDetails(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-details'
    lookup_field = 'pk'
    permission_classes = (IsOwnerUserOrReadOnly,
                          IsSuperUser,)


class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'
    permission_classes = (IsAuthenticated,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-details'
    permission_classes = (IsOwnerProfileOrReadOnly,
                          IsAuthenticated,)


class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    name = 'ad-list'
    permission_classes = (IsAuthenticated,)


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    name = 'ad-details'
    permission_classes = (IsAuthenticated,)


class MessagesList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    name = 'messages-list'
    # permission_classes = (IsAuthenticated,)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    name = 'message-details'
    # permission_classes = (IsAuthenticated,)


class ApiRoot(generics.GenericAPIView):
    name = 'API'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'documentation': reverse('documentation', request=request),
                'users': reverse(UserList.name, request=request),
                'profiles': reverse(ProfilesList.name, request=request),
                'ads': reverse(AdList.name, request=request),
                'messages': reverse(MessagesList.name, request=request),
            }
        )
