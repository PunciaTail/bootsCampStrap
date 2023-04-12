from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user"

    follow = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='follower')
    bio = models.TextField("자기소개", blank=True)
    imgfile = models.ImageField(null=True, upload_to="user_images", blank=True)


    def __str__(self):
        return self.username
    