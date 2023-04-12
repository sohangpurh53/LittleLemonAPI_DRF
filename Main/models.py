from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index = True)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=255, db_index = True)
    price = models.FloatField(db_index = True)
    featured = models.BooleanField(db_index = True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.FloatField(db_index = True) 
    unitPrice = models.FloatField(db_index = True)

    class Meta:
        unique_together = ('user','item')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deliveryCrew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='deliver_crew', null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.FloatField(db_index = True)
    date = models.DateField(db_index=True)

class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.FloatField(db_index = True) 
    unitPrice = models.FloatField(db_index = True)

    class Meta:
        unique_together = ('order','item')