from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food')
)
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity = models.IntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}  {self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    staff = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

    class Meta:
        verbose_name_plural = 'Order'

