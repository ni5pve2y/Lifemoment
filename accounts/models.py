from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

        second_friend, second_created = cls.objects.get_or_create(
            current_user=new_friend
        )
        second_friend.users.add(current_user)


class UserProfile(models.Model):
    user = models.OneToOneField(User, editable=False)
    image = models.ImageField(null=True)

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
