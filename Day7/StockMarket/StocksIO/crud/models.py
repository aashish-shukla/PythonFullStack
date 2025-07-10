from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    curr_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ticker} - {self.name}"

class UserStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='user_stocks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_stocks')
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    purchase_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.stock.ticker} ({self.purchase_quantity})"
