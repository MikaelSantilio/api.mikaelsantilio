from django.contrib import admin
from core.models import Service, Project


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active', 'updated_at')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'active', 'updated_at')
