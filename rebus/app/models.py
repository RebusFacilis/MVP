from django.db import models
from django.contrib.auth.models import User

PAYMENT_MODE = (
    ('6','6 meses'),
    ('12','12 meses'),
    ('18','18 meses'),
    ('24','24 meses')
)

class CreditCard(models.Model):
    token = models.CharField(max_length=200)
    user = models.ForeignKey(User)


class Invenstment(models.Model):
    monthly_payment = models.FloatField()
    payment_mode = models.CharField(max_length=30, choices=PAYMENT_MODE)
    objective = models.FloatField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User)
