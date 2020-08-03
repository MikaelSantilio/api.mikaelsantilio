from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from core.forms import ContactForm
from core.models import Service, Project
from core.serializers import ServiceSerializer, ProjectSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class SendEmail(APIView):

    def post(self, request, format=None):
        form = ContactForm(request.data)
        if form.is_valid():
            form.send_email()
            return Response({'success': 'Email enviado'}, status=status.HTTP_200_OK)
        else:
            errors = {field: errors[0] for field, errors in form.errors.items()}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceList(generics.ListAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny, )


class ServiceCreate(generics.CreateAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )


class ProjectList(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )


class ProjectCreate(generics.CreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )
