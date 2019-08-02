from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser



class PariSport(AbstractBaseUser):
    cagnote     = models.DecimalField(max_digits=8, decimal_places=2)
    coteEquip1  = models.DecimalField(max_digits=5, decimal_places=2)
    miseEquip1  = models.DecimalField(max_digits=7, decimal_places=2)
    coteEquip2  = models.DecimalField(max_digits=5, decimal_places=2)
    miseEquip2  = models.DecimalField(max_digits=7, decimal_places=2)
    gainEquip1  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beneficeEquip1  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gainEquip2  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beneficeEquip2  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    authorId 	= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.cagnote