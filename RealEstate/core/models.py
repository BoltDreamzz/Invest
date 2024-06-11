from django.db import models
from userauths.models import User

class InvestmentPlan(models.Model):
    title = models.CharField(max_length=255)
    min_amount = models.CharField(max_length=4)
    max_amount = models.CharField(max_length=12)
    validity = models.CharField(max_length=6)
    
    def __str__(self):
        return self.title
    
    
class Property(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='prop_images')
    rating = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.name

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.property.name}'
