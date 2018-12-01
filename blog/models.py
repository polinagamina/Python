from django.db import models
from django.utils import timezone

class Agreement(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID', blank=False)
    FIO = models.CharField(max_length=100, blank=False)
    Service = models.CharField(max_length=100, blank=False)
    Price = models.CharField(max_length=100)
    Kind = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)



    def publish(self):
        self.save()

    def __str__(self):
        return self.id

class Request(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID', blank=False)
    FIO = models.CharField(max_length=100, blank=False)
    Service = models.CharField(max_length=100, blank=False)
    Telephone = models.CharField(max_length=20)
    Email = models.EmailField(blank=True)


    def publish(self):
        self.save()

    def __str__(self):
        return self.id

class RegAgreement(models.Model):
    id = models.CharField(max_length=20, primary_key=True,verbose_name='ID',serialize=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    FIO = models.CharField(max_length=100, blank=False)
    OI = models.CharField(max_length=100, blank=False)
    Kind = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.id

class RegRequest(models.Model):
    id = models.CharField(max_length=20, primary_key=True,verbose_name='ID',serialize=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    FIO = models.CharField(max_length=100, blank=False)
    Service = models.CharField(max_length=100, blank=False)
    State = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.id
