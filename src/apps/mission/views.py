from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError

from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def perform_destroy(self, instance):
        if instance.cat:
            raise ValidationError("Cannot delete a mission that is assigned to a cat.")
        instance.delete()


class TargetViewSet(ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.completed and 'notes' in self.request.data:
            raise ValidationError("Cannot update notes for a completed target.")
        serializer.save()
