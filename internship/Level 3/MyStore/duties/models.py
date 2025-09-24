from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=50)   
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Rands per m³
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # NEW

    def __str__(self):
        return f"{self.name} ({self.strength})"

