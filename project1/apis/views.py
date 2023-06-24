from django.shortcuts import render
from rest_framework .response import Response
from rest_framework.views import APIView
from .serializer import *
from app1.models import*

# Create your views here.
class ResumeView(APIView):
    def get(self, request):
        resume_obj=Resume.objects.all()
        serializer=ResumeSerializer(resume_obj, many=True)
        return Response({
            'Status':True,
            'massage':'Resume data Fetched',
            'data':serializer.data
        })
    def post(self,request):
        try:
            data=request.data
            serializer=ResumeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Status':True,
                    'massage':'Success data',
                    'data':serializer.data
                })
            return Response({
                'Status':False,
                'massage':'Invalid data ',
                'data':serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'Status':False,
                'massage':'Some thing went wrong',
            })

