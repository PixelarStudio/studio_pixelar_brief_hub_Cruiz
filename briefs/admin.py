from django.contrib import admin
from .models import Brief

@admin.register(Brief)
class BriefAdmin(admin.ModelAdmin):
    list_display = ("title", "client_name", "service_type", "created_at", "owner")
    search_fields = ("title", "client_name", "service_type")
