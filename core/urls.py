from django.urls import path, include
from core.views import (
    UserList,
    UserDetails,
    ProfilesList,
    ProfileDetail,
    ItemList,
    ItemDetail,
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
    path('itens/', ItemList.as_view(), name='item-list'),
    path('itens/<int:pk>', ItemDetail.as_view(), name='item-details'),
    path('api-auth/', include('rest_framework.urls')),
]