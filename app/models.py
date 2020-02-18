from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    photoUrl = models.URLField()


class Conversation(models.Model):
    photoUrl = models.URLField()
    name = models.CharField(max_length=50)
    recent_text = models.CharField(max_length=2048)
    last_time = models.DateTimeField()
    unread_count = models.IntegerField()


class Message(models.Model):
    message = models.CharField(max_length=2048)
    attachment_url = models.URLField()
    from_user = models.BigIntegerField()
    to_user = models.BigIntegerField()


class Group(models.Model):
    photo_url = models.URLField()
    name = models.CharField(max_length=50)
    group_id = models.BigIntegerField()
    members = models.ManyToManyField(User, through='Membership')


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField()

