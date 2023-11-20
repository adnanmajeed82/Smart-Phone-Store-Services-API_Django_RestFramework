from django.db import models

class Smartphone(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.OneToOneField('Bill', on_delete=models.SET_NULL, null=True, blank=True, related_name='order_billing')

class Bill(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='bill_order')
    content = models.TextField()

class Receipt(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    save_location = models.FileField(upload_to='receipts/')
