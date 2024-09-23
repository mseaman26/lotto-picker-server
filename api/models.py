from django.db import models
from django.contrib.auth.models import User  # Import the User model
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class LottoPick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate with User
    numbers = models.CharField(max_length=255)  # Store numbers as a comma-separated string
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.numbers)