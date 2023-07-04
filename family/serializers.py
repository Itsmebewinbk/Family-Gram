from rest_framework import serializers

from family.models import Family, Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"


class FamilySerializer(serializers.ModelSerializer):
    # nodes = NodeSerializer(many=True)

    class Meta:
        model = Family
        fields = ("id", "name",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        nodes = (
            instance.members.all()
        )  # Get all nodes related to the Family instance
        data["nodes"] = NodeSerializer(
            nodes, many=True
        ).data  # Serialize the nodes
        return data
