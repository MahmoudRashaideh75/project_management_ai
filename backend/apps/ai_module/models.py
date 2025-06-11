from django.db import models
from django.contrib.postgres.fields import JSONField

# Domains of projects this assistant can be trained on.
# Kept minimal as an example set of choices.
DOMAIN_CHOICES = [
    ("software", "Software"),
    ("construction", "Construction"),
    ("finance", "Finance"),
    ("general", "General"),
]

class AIProjectAssistant(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    context = JSONField(help_text="Current conversation context")
    memory = models.TextField(help_text="Long-term memory storage")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project'], 
                name='unique_assistant_per_project'
            )
        ]

class AITrainingData(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    source = models.CharField(max_length=100)
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES)
    version = models.CharField(max_length=20)
