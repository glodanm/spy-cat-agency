from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Target, Mission


@receiver(post_save, sender=Target)
def check_mission_completed(sender, instance, **kwargs):
    mission = instance.mission
    if all(target.completed for target in mission.targets.all()):
        mission.completed = True
        mission.save()
