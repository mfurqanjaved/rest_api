from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name + " - $" + str(self.price) + " - " + self.description