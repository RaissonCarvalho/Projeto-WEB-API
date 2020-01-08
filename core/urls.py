from django.urls import path, include
from core.views import (
    UserList,
    UserDetails,
    ProfilesList,
    ProfileDetail,
    AdList,
    AdDetail,
    MessagesList,
    MessageDetail,
    ChatList,
    ChatDetails,
    ApiRoot
)
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('docs/', schema_view, name='documentation'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetails.as_view(), name='user-details'),
    path('profiles/', ProfilesList.as_view(), name='profile-list'),
    path('profiles/<int:pk>', ProfileDetail.as_view(), name='profile-details'),
    path('ads/', AdList.as_view(), name='ad-list'),
    path('ads/<int:pk>', AdDetail.as_view(), name='ad-details'),
    path('messages/', MessagesList.as_view(), name='messages-list'),
    path('messages/<int:pk>', MessageDetail.as_view(), name='message-details'),
    path('chats/', ChatList.as_view(), name='chat-list'),
    path('chats/<int:pk>', ChatDetails.as_view(), name='chat-details'),
    path('api-auth/', include('rest_auth.urls')),
    path('api-auth/token', obtain_jwt_token),
    path('api-auth/refresh-token', refresh_jwt_token),
]