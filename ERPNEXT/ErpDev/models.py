from dataclasses import Field

from django.core import exceptions
from django.db import models
from django.forms import forms
from django.utils import timezone
from .validation import validate_range
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ListTodo(models.Model):
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(Category,default="general",on_delete=models.PROTECT)  # a foreignkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called


# Creating the necessary columns for inserting the database files

class OnlineShopperTable(models.Model):
    Visitor_type_list = [('Returning', 'Returning_Visitor'), ('New', 'New_Visitor'), ('Other', 'Other')]
    Bool_Values = [('False', 'FALSE'), ('True', 'TRUE')]
    Administrative = models.IntegerField(default=0)
    Administrative_Duration = models.FloatField(default=0)
    Informational = models.IntegerField(default=0)
    Informational_Duration = models.FloatField(default=0)
    ProductRelated = models.FloatField(default=0)
    ProductRelated_Duration = models.FloatField(default=0)
    BounceRates = models.FloatField(default=0)
    ExitRates = models.FloatField(default=0)
    PageValues = models.FloatField(default=0)
    SpecialDay = models.DecimalField(default=0, max_digits=3, decimal_places=2,
                                     validators=[MaxValueValidator(1), MinValueValidator(0)])
    Month = models.CharField(max_length=15)
    OperatingSystems = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(8)])
    Browser = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(13)])
    Region = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(9)])
    TrafficType = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(20)])
    Visitor_type = models.CharField(choices=Visitor_type_list, max_length=50)
    Weekend = models.CharField(choices=Bool_Values, max_length=50)
    Revenue = models.CharField(choices=Bool_Values, max_length=50)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
