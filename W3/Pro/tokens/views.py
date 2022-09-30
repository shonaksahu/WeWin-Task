
from unicodedata import name
from django.shortcuts import render
from django.http import JsonResponse
from httplib2 import Response
from .models import Register
from .serializers import RegisterSerialiazers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def register_list(request):
    if request.method == 'GET':
        register = Register.objects.all()
        serializer = RegisterSerialiazers(register, many=True)
        return JsonResponse({'register' : serializer.data})

    if request.method == 'POST':
        serializer = RegisterSerialiazers(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def register_detail(request, id):
    try:
        register = Register.objects.get(pk=id)
    except Register.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RegisterSerialiazers(register)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RegisterSerialiazers(register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


