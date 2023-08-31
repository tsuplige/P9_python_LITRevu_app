from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    def __str__(self):
        return f'{self.title}'
    is_ticket = models.BooleanField(default=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    have_review = models.BooleanField(default=False)


class Review(models.Model):
    def __str__(self):
        return f'{self.headline}'
    is_ticket = models.BooleanField(default=False)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='following')

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='followed_by')

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )

    @classmethod
    def follow(cls, user, followed_user):
        if not cls.objects.filter(user=user,
                                  followed_user=followed_user).exists():
            cls.objects.create(user=user, followed_user=followed_user)

    @classmethod
    def unfollow(cls, user, followed_user):
        cls.objects.filter(user=user, followed_user=followed_user).delete()

    def __str__(self):
        return f'{self.user} follows {self.followed_user}'
