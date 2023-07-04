from django.urls import path
from family.views import *


urlpatterns = [
   
    path("node/", NodeListCreateView.as_view()),
    path("node/<int:pk>/", NodeUpdateView.as_view()),
]
