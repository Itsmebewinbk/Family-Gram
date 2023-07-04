from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from family.serializers import NodeSerializer
from family.models import Node



class NodeListCreateView(ListCreateAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()


class NodeUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()
