from django.db import models

# Create your models here.


class MightyPayment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=255)
    description = models.TextField()
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    payment_request_id = models.CharField(max_length=255)
    payment_request_status = models.CharField(max_length=255)
    payment_request_longurl = models.CharField(max_length=255)
    payment_request_shorturl = models.CharField(max_length=255)

    def __str__(self):
        return self.name

