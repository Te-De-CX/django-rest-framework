from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.permissions import IsAuthenticated
from app.models import Student
from app.serializers import StudentSerializer

class TesView(APIView):
    # def get(self,request,*args, **kwargs):
    #     data = {
    #         'username': 'admin',
    #         'years_active':10
    #     }
    #     return Response(data)
    
    permission_classes = (IsAuthenticated,)
    
    def get(self,request,*args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)