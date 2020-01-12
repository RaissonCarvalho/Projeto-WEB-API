from core.models import *
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    url = HyperlinkedIdentityField(
        view_name='user-details',
        lookup_field='pk'
    )

    class Meta:
        model = User
        fields = (
            'url',
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
            'id',
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

        password = make_password("123")
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['first_name'] + validated_data['last_name'],
            email=validated_data['email'],
            password=password)

        return Profile.objects.create(
            user_id=user.id,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=user.email,
            phone_number=validated_data['phone_number'],
            city=validated_data['city']
        )

    @staticmethod
    def validate_password(value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class AdSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='ad-details',
        lookup_field='pk'
    )
    pub_date = serializers.ReadOnlyField(read_only=True)
    owner = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Ad
        fields = (
            'id',
            'url',
            'title',
            'description',
            'value',
            'pub_date',
            'owner',
        )

    # def create(self, validated_data):
    #     return Ad.objects.create(
    #         title=validated_data['title'],
    #         description=validated_data['description'],
    #         value=validated_data['value'],
    #         owner=validated_data['owner'],
    #     )


class MessageSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='message-details',
        lookup_field='pk'
    )

    related_ad = serializers.SlugRelatedField(queryset=Ad.objects.all(), slug_field='title')
    sender_profile = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    reciver_profile = serializers.SlugRelatedField(slug_field='first_name', read_only=True)

    class Meta:
        model = Message
        fields = (
            'url',
            'related_ad',
            'content',
            'sender_profile',
            'reciver_profile',
            'time',
        )


class ChatSerializer(ModelSerializer):
    message = serializers.SlugRelatedField(queryset=Message.objects.all(), slug_field='content')

    class Meta:
        model = Chat
        fields = (
            'message'
        )