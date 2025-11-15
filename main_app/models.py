from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_path = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=100)  # Doctor's name
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='doctors')
    image = models.ImageField(blank=True)   
    is_available = models.BooleanField(default=True) 

    def __str__(self):
        return self.name


# Create your models here.

class Appointment(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")

    doctor = models.ForeignKey("main_app.Doctor", on_delete=models.CASCADE, related_name="appointments")

    address = models.TextField()
    number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("doctor", "appointment_date", "appointment_time")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} → {self.doctor.name} on {self.appointment_date} at {self.appointment_time}"
 




