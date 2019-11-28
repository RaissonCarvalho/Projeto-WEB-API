from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from core.serializers import *
from core.models import *


class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-details'


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    name = 'item-list'


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    name = 'item-details'


class ApiRoot(generics.GenericAPIView):
    name = 'API'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'profiles': reverse(ProfilesList.name, request=request),
                'itens': reverse(ItemList.name, request=request),
                'documentation': reverse('documentation', request=request)
            }
        )