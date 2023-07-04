from django.urls import path
from family.views import *


urlpatterns = [
    path("family/", FamilyListCreateAPIView.as_view()),
    path("node/", NodeListCreateAPIView.as_view()),
    path("node/<int:pk>/", NodeUpdateView.as_view()),
]
