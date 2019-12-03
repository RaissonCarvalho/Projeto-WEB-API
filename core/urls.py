from django.urls import path, include
from core.views import (
    UserList,
    UserDetails,
    ProfilesList,
    ProfileDetail,
    AdList,
    AdDetail,
    ApiRoot
)
from rest_framework_swagger.views import get_swagger_view

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
    path('api-auth/', include('rest_framework.urls')),
]