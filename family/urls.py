from django.urls import path
from family.views import *


urlpatterns = [
    path("family/", FamilyCreateView.as_view()),
    path("family/<int:pk>/", FamilyDetailView.as_view()),
    path("node/", NodeListCreateView.as_view()),
    path("node/<int:pk>/", NodeUpdateView.as_view()),
]
