from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.species}"


class Appointment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.animal.name} on {self.appointment_date}"


class Medication(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.medicine_name} for {self.animal.name}"


class Note(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    staff_member = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.appointment.animal.name} by {self.staff_member} on {self.created_at}"
