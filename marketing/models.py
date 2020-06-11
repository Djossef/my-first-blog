from django.db import models


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Like(models.Model):
    likeField = models.CharField(max_length=255)

    def __str__(self):
        return self.likeField
