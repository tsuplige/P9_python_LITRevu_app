from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import UserFollows


class User(AbstractUser):
    def follow(self, followed_user):
        UserFollows.follow(self, followed_user)

    def unfollow(self, followed_user):
        UserFollows.unfollow(self, followed_user)
