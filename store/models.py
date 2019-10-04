import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    
    product_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Price(models.Model):

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_int = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text