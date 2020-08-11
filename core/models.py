from django.db import models
# from sorl.thumbnail import ImageField


class Base(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Service(Base):
    icon = models.URLField()
    title = models.CharField(max_length=18)
    description = models.CharField(max_length=116)

    def __str__(self):
        return f'Service - {self.title}'


class Project(Base):
    thumb = models.URLField()
    title = models.CharField(max_length=23)
    subtitle = models.CharField(max_length=32)
    description = models.CharField(max_length=116)
    link = models.CharField(max_length=128)

    def __str__(self):
        return f'Project - {self.title}({self.subtitle})'
