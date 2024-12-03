from rest_framework import serializers

from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'completed']

    def validate(self, data):
        if data.get("completed") and self.instance and self.instance.completed:
            raise serializers.ValidationError("Cannot update notes for a completed target.")
        return data


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'targets', 'completed']

    def validate(self, data):
        targets = data.get('targets', [])
        if not (1 <= len(targets) <= 3):
            raise serializers.ValidationError("A mission must have between 1 and 3 targets.")
        return data

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission
    
    
    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', [])

        instance.cat = validated_data.get('cat', instance.cat)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()

        existing_targets = {target.id: target for target in instance.targets.all()} 
        new_targets = [] 

        for target_data in targets_data:
            target_id = target_data.get('id')
            if target_id:
                if target_id in existing_targets:
                    target_instance = existing_targets.pop(target_id)
                    for attr, value in target_data.items():
                        setattr(target_instance, attr, value)
                    target_instance.save()
                else:
                    raise ValueError(f"Target ID {target_id} does not exist in this mission.")
            else:
                new_targets.append(target_data)

        for target_data in new_targets:
            Target.objects.create(mission=instance, **target_data)

        for remaining_target in existing_targets.values():
            remaining_target.delete()

        return instance
