from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("companies", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name_plural = 'companies' 
    


class Gig(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=250)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("gig_detail", kwargs={"pk": self.pk})
    