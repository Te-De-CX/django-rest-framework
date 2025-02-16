# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer

# class TesView(APIView):
#     def get(self,request,*args, **kwargs):
#         data = {
#             'username': 'admin',
#             'years_active':10
#         }
#         return Response(data)
    
# def post(self,request,*args,**kwargs):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from app.models import Student
# from app.serializers import StudentSerializer

# class TesView(APIView):
#     # def get(self,request,*args, **kwargs):
#     #     data = {
#     #         'username': 'admin',
#     #         'years_active':10
#     #     }
#     #     return Response(data)
#     def get(self,request,*args, **kwargs):
#         qs = Student.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self,request,*args,**kwargs):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)