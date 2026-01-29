from django.db import models
from django.contrib.auth.models import User

class FormSchema(models.Model):
    """
    Stores the structure of the dynamic form.
    We assume there's one active schema called 'default' or similar, 
    but this allows for multiple versions if needed.
    """
    name = models.CharField(max_length=100, default="Dynamic Form")
    schema_data = models.JSONField(default=list)  # list of field definitions (label, type, etc.)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    # common fields that every employee might have
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
    # store dynamic field values here.
    dynamic_data = models.JSONField(default=dict, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
