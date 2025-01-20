from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



class Status(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Priority_level(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=models.CASCADE,
        related_name="assignee"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
    )
    priority_level = models.ForeignKey(
        Priority_level,
        on_delete=models.CASCADE,
    )
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.summary
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
    
# Create your models here.
