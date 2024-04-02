from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializer import ProjectSerializer
# Create your views here.
class ProjectView(APIView):
    def get(self,request):
        proj = Project.objects.all()
        serialize = ProjectSerializer(proj,many=True)
        return Response(serialize.data)