from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["time_created"]
    
    def __str__(self) -> str:
        return f"{self.name}'s tweet"