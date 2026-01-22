from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PromptTemplate
from .serializers import PromptTemplateSerializer

class PromptListView(APIView):
    def get(self, request):
        prompts = PromptTemplate.objects.all().order_by('-created_at')
        serializer = PromptTemplateSerializer(prompts, many=True)
        return Response(serializer.data)