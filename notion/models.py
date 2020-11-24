from django.db import models
from django.utils import timezone

class Post(models.Model):
    name = models.CharField(max_length=1000, null=True)
    text = models.TextField(null=True)
    # pw = models.CharField(max_length=32, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

