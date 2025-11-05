from django.urls import path
from .views import (
    BriefListView,
    BriefDetailView,
    BriefCreateView,
    BriefUpdateView,
    BriefDeleteView,
)

urlpatterns = [
    path("", BriefListView.as_view(), name="brief_list"),              # /pages/
    path("create/", BriefCreateView.as_view(), name="brief_create"),
    path("<int:pk>/", BriefDetailView.as_view(), name="brief_detail"),
    path("<int:pk>/edit/", BriefUpdateView.as_view(), name="brief_update"),
    path("<int:pk>/delete/", BriefDeleteView.as_view(), name="brief_delete"),
]
