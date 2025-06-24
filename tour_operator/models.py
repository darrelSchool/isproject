from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import CASCADE
from django.db.models.fields import uuid

# Create your models here.


class Operator(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=45)
    email = models.EmailField()
    description = models.TextField()
    banned = models.BooleanField(default=False)


class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=False)
    visibility = models.BooleanField(default=False)
    author = models.ForeignKey(Operator, on_delete=models.DO_NOTHING, null=False)
