from rest_framework.generics import ListAPIView
from backend.demo.models import Demo, Project, MLHMember
from .serializers import DemoSerializer,ProjectSerializer, MemberSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class DemoListView(ListAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer


class ProjectListView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MemberListView(viewsets.ModelViewSet):

    queryset = MLHMember.objects.all()
    serializer_class = MemberSerializer
