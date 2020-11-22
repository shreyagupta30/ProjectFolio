from rest_framework.generics import ListAPIView
from backend.demo.models import Demo, Project, MLHMember, Commit
from .serializers import DemoSerializer,ProjectSerializer, MemberSerializer, CommitSerializer
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

class CommitListView(viewsets.ModelViewSet):

    queryset = Commit.objects.all()
    serializer_class = CommitSerializer

    def get_queryset(self):
        req = self.request
        print(req)
        project = req.query_params.get('project', None)
        if project:
            self.queryset = Commit.objects.filter(project=project)
        return self.queryset

