from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FoodCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class EssNutr(models.Model):
    food = models.CharField(max_length=100)
    kcal = models.IntegerField()
    proteins = models.DecimalField(max_digits=4, decimal_places=1)
    fats = models.DecimalField(max_digits=4, decimal_places=1)
    carbohydrates = models.DecimalField(max_digits=4, decimal_places=1)
    f_category = models.ForeignKey(FoodCategory)

    def __str__(self):
        return self.food


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    
    GENDER_CHOICES = [(x, x) for x in ['male', 'female']]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    choices = models.ForeignKey(EssNutr)

    def __str__(self):
        return self.user.username