from rest_framework import serializers

from family.models import Family, Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["spouse"] = None
        if instance.spouse:
            data["spouse"] = {
                "id": instance.spouse.id,
                "name": instance.spouse.name,
            }
        data["children"] = NodeSerializer(instance.children.all(), many=True).data
        return data


class FamilySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Family
        fields = ("id", "name",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
    
        data["nodes"] = NodeSerializer(instance.members, many=True).data

        return data
