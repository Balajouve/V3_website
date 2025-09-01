from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=120)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.client_name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.question

class Lead(models.Model):
    INSURANCE_TYPES = [('health','Health'),('life','Life'),('vehicle','Vehicle'),('business','Business')]
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    insurance_type = models.CharField(max_length=20, choices=INSURANCE_TYPES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} ({self.insurance_type})"
