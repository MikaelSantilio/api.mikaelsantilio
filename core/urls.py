from django.urls import path
from core import views

urlpatterns = [
    path('services/', views.ServiceList.as_view(), name='service-list'),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),

    path('projects/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectDetail.as_view()),

    path('email/', views.SendEmail.as_view(), name='email')
]
