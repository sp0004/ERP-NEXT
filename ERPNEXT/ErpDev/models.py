from dataclasses import Field

from django.core import exceptions
from django.db import models
from django.forms import forms

from .validation import validate_range
from django.core.validators import MaxValueValidator, MinValueValidator



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
    Weekend = models.BooleanField()
    Revenue = models.BooleanField()


# Overiding the Boolean Value
def to_python(self, value):
    if self.null and value in self.empty_values:
        return None
    if value in (True, False):
        # 1/0 are equal to True/False. bool() converts former to latter.
        return bool(value)
    if value in ('t', 'True', '1', 'TRUE'):
        return True
    if value in ('f', 'False', '0', 'FALSE'):
        return False
    raise exceptions.ValidationError(
        self.error_messages['invalid_nullable' if self.null else 'invalid'],
        code='invalid',
        params={'value': value},
    )

