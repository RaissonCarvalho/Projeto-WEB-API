from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=11)
    city = models.CharField(max_length=30)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Item(models.Model):
    owner = models.ForeignKey('Profile', related_name='profile', on_delete=models.CASCADE)
    description = models.TextField()
    value = models.FloatField()


class Ad(models.Model):
    title = models.CharField(max_length=30)
    item = models.OneToOneField('Item', related_name='ad_item', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    sender_profile = models.OneToOneField('Profile', related_name='sender', on_delete=models.CASCADE)
    reciver_profile = models.OneToOneField('Profile', related_name='reciver', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', related_name='message', on_delete=models.CASCADE)