from rest_framework import serializers
from core.models import Service, Project
from easy_thumbnails.templatetags.thumbnail import thumbnail_url


class ThumbnailSerializer(serializers.URLField):
    def __init__(self, alias, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_only = True
        self.alias = alias

    def to_representation(self, value):
        if not value:
            return None

        url = thumbnail_url(value, self.alias)
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Service
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Project
        fields = '__all__'
