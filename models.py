from django.db import models

# Create your models here.
class Forum(models.Model):
    question = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    reply = models.BooleanField(default=False)

    def __str__(self):
        return self.question