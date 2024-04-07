from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)  # Otomatik artan bir id sütunu
    name = models.CharField(max_length=100)  # Karakter dizisi olarak ad alanı
    email = models.EmailField(unique=True)   # E-posta alanı (benzersiz olmalı)
    password = models.CharField(max_length=100)  # Parola alanı
    birth_date = models.DateField()   # Tarih alanı (doğum tarihi)

    def __str__(self):
        return self.name  # Django admin panelinde nesnelerin adlarını göstermek için kullanılır
