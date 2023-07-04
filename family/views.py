from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from family.serializers import FamilySerializer, NodeSerializer
from family.models import Family, Node


class FamilyCreateView(CreateAPIView):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()


class FamilyDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()


class NodeListCreateView(ListCreateAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()


class NodeUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()
