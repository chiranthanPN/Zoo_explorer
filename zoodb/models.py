from django.db import models

class animals(models.Model):
    name = models.CharField(max_length=100)
    animal_id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    food = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)

class doner(models.Model):
    name = models.CharField(max_length=100)
    doner_id = models.CharField(max_length=20, primary_key=True)
    age = models.IntegerField()
    animal = models.CharField(max_length=100)
    phone = models.BigIntegerField()

class caretaker(models.Model):
    name = models.CharField(max_length=100)
    caretaker_id = models.CharField(max_length=30, primary_key=True)
    age = models.IntegerField()
    exp = models.IntegerField()
    phone = models.BigIntegerField()

class enrollments(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    animal_id = models.ForeignKey(animals, on_delete=models.CASCADE)
    doner_id = models.ForeignKey(doner, on_delete=models.CASCADE)
    caretaker_id = models.ForeignKey(caretaker, on_delete=models.CASCADE)
