from rest_framework import serializers
from backend.demo.models import Demo, Project, MLHMember


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MLHMember
        fields = '__all__'