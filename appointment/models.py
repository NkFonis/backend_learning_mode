from django.db import models

# Create your models here.
class Doctor(models.Model):
    specialty = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.specialty
    
class Patient(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    choosen_time = models.DateField()
    doc = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    sym_des=models.TextField()



