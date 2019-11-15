from django.db import models
from .validation import validate_range
from django.core.validators import MaxValueValidator, MinValueValidator


# Creating the necessary columns for inserting the database files

class OnlineShopperTable(models.Model):
    Visitor_type_list = [('Returning','Returning_Visitor'), ('New','New_Visitor'), ('Other','Other')]
    Administrative = models.IntegerField(default=0)
    Administrative_Duration = models.IntegerField(default=0)
    Informational = models.IntegerField(default=0)
    Informational_Duration = models.FloatField(default=0)
    ProductRelated = models.IntegerField(default=0)
    ProductRelated_Duration = models.FloatField(default=0)
    BounceRates = models.FloatField(default=0)
    ExitRates = models.FloatField(default=0)
    PageValues = models.FloatField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    Month = models.CharField(max_length=15)
    OperatingSystems = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(8)])
    Browser = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(13)])
    Region = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(9)])
    TrafficType = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(20)])
    Visitor_type = models.CharField(choices=Visitor_type_list, max_length= 50)
    Weekend = models.BooleanField()
    Revenue = models.BooleanField()
