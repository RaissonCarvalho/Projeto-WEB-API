from core.models import *
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from rest_framework import serializers


class ProfileSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='profile-details',
        lookup_field='pk'
    )

    class Meta:
        model = Profile
        fields = (
            'url',
            'first_name',
            'last_name',
            'phone_number',
            'city',
            'email',
        )

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['first_name']+validated_data['last_name'],
            email=validated_data['email'],
            password='123')

        return Profile.objects.create(
            user_id=user.id,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=user.email,
            phone_number=validated_data['phone_number'],
            city=validated_data['city']
        )

class ItemSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='item-details',
        lookup_field='pk'
    )
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='profile-details', read_only=True)
    owner_name = serializers.ReadOnlyField(source='owner.first_name')

    class Meta:
        model = Item
        fields = (
            'url',
            'owner',
            'owner_name',
            'description',
            'value'
        )

    def create(self, validated_data):
        return Item.objects.create(
            owner=validated_data['owner'],
            description=validated_data['description'],
            value=validated_data['value']
        )
