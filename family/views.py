from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from family.serializers import FamilySerializer, NodeSerializer
from family.models import Family, Node


class FamilyListCreateAPIView(ListCreateAPIView):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()



class NodeListCreateAPIView(ListCreateAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()

class NodeUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()
