# donations/models.py

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=datetime.now)  # Default value set to current datetime

    def __str__(self):
        return self.title


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    referral_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    referred_by = models.ForeignKey(
        'self', related_name='referred_donors', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.user.username

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.donor} donated ${self.amount} to {self.campaign}"
