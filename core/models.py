from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=11)
    city = models.CharField(max_length=30)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Ad(models.Model):
    owner = models.ForeignKey('Profile', related_name='ads', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    value = models.FloatField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']


class Message(models.Model):
    related_ad = models.OneToOneField('Ad', related_name='related_ad', on_delete=models.CASCADE, default=None)
    sender_profile = models.OneToOneField('Profile', related_name='sender_messages', on_delete=models.CASCADE)
    reciver_profile = models.OneToOneField('Profile', related_name='reciver_messages', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time']


class Chat(models.Model):
    message = models.ForeignKey('Message', related_name='message', on_delete=models.CASCADE)