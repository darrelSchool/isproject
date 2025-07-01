from django.db import models

from tour_operator.models import Operator, Package


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    title = models.CharField(max_length=50)


class Quote(models.Model):
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING, null=False)
    author = models.ForeignKey(Operator, on_delete=models.DO_NOTHING, null=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    adults_no = models.DecimalField(max_digits=3, decimal_places=0)
    child_no = models.DecimalField(max_digits=3, decimal_places=0)
    nights_no = models.DecimalField(max_digits=3, decimal_places=0)
    date_created = models.DateTimeField(auto_now=True)
    date_chosen = models.DateField()
    resolved = models.BooleanField(default=False)
