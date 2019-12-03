from core.models import *
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from rest_framework import serializers


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'date_joined',
        )


class ProfileAdSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='ad-details',
        lookup_field='pk'
    )

    class Meta:
        model = Ad
        fields = (
            'url',
            'title'
        )


class ProfileSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='profile-details',
        lookup_field='pk'
    )

    ads = ProfileAdSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            'url',
            'first_name',
            'last_name',
            'phone_number',
            'city',
            'email',
            'ads',
        )

    def create(self, validated_data):
        users = User.objects.all()
        for user in users:
            if validated_data['email'] in user.email:
                raise serializers.ValidationError('Email already exists')
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


class AdSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='ad-details',
        lookup_field='pk'
    )
    pub_date = serializers.ReadOnlyField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.first_name')
    profile = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Ad
        fields = (
            'url',
            'title',
            'description',
            'value',
            'pub_date',
            'owner',
            'profile'
        )

    def create(self, validated_data):
        return Ad.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            value=validated_data['value'],
            owner=validated_data['owner'],
        )


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = (
            'content',
            'time'
        )