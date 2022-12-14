from django.db import models
from authentication.models import User

# Create your models here.
class Donasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    pesan = models.CharField(max_length=255)

    class Meta:
        ordering = ["-pk"]
