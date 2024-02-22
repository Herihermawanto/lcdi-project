from django.db import models

# Create your models here.
class Tweet(models.Model):
    postTweet   = models.TextField(max_length=140)

    def __str__(self):
        return self.postTweet