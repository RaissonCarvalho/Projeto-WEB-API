from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import status
from core.permissions import *
from core.serializers import *
from core.models import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    # permission_classes = (IsSuperUser,)


class UserDetails(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-details'
    lookup_field = 'pk'
    # permission_classes = (IsOwnerUserOrReadOnly,
                          # IsSuperUser,)


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
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        sender_profile = Profile.objects.get(email=self.request.user.email)
        ad = Ad.objects.get(title=self.request.data['related_ad'])
        reciver_profile = ad.owner

        if sender_profile == reciver_profile:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        chats = Chat.objects.all()
        for chat in chats:
            if chats == None:
                message = Message.objects.create(sender_profile=sender_profile,
                                                 reciver_profile=reciver_profile,
                                                 content=self.request.data['content'],
                                                 related_ad=ad)
                Chat.objects.create(
                    message=message
                )

                serializer.save(
                    sender_profile=sender_profile,
                    reciver_profile=reciver_profile,
                    content=self.request.data['content'],
                    related_ad=ad
                )
            elif chat.message.sender_profile == sender_profile and chat.message.related_ad == ad:
                message = Message.objects.create(sender_profile=sender_profile,
                reciver_profile=reciver_profile,
                content=self.request.data['content'],
                related_ad=ad)
                Chat.objects.create(
                    message=message
                )

                serializer.save(
                    sender_profile=sender_profile,
                    reciver_profile=reciver_profile,
                    content=self.request.data['content'],
                    related_ad=ad
                )
        else:
            serializer.save(
                sender_profile=sender_profile,
                reciver_profile=reciver_profile,
                content=self.request.data['content'],
                related_ad=ad
            )


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    name = 'message-details'
    permission_classes = (IsAuthenticated,)


class ChatList(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    name = 'chat-list'


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    name = 'chat-details'


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
                'chat': reverse(ChatList.name, request=request)
            }
        )
