from django.db import models

from apps.cats.models import SpyCat


class Mission(models.Model):
    cat = models.OneToOneField(SpyCat, on_delete=models.PROTECT, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name if self.cat else 'Unassigned'}"


class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
