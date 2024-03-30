from django.db import models
from datetime import datetime

# Create your models here.



class Comments(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    comment_text = models.CharField(max_length=140)
    timestamp = models.DateTimeField(default=datetime.now())

    likes = models.PositiveIntegerField(default=0)

    # When i get the Comms obj by default the order is asc
    # To get the comms by the latest posted imma do a Meta Class
    # Ordering by the timestamp

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp'])
        ]
