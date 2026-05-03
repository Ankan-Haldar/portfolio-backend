from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Skill
from .serializers import ProjectSerializer, SkillSerializer


class ProjectAPI(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class SkillAPI(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)