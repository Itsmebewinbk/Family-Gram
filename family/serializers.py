from rest_framework import serializers

from family.models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ("id", "name", "parent", "spouse")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["spouse"] = None
        if instance.spouse:
            data["spouse"] = {
                "id": instance.spouse.id,
                "name": instance.spouse.name,
            }
        data["children"] = NodeSerializer(
            instance.parent.all(), many=True
        ).data
        return data


