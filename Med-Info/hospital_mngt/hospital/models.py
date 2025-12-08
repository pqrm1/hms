from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    special=models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.name} - {self.special}"

class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    address=models.TextField()

    def __str__(self):
        return f"{self.name} ({self.gender}) - {self.mobile or 'No mobile'}"

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return f"{self.doctor} with {self.patient} on {self.date} at {self.time.strftime('%I:%M %p')}"

