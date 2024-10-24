# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template import loader

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.

# def tasks(request):
#     # return HttpResponse("these are my tasks")
#     template = loader.get_template('tasks_page.html')
#     return HttpResponse(template.render())


# def users(request):
#     return HttpResponse("these are my users")

# def home(request):
#     return HttpResponse("Welcome to the home page!")
@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all  products, or create a new product.
    """
    if request.method == 'GET':
        products = Task.objects.all()
        serializer = TaskSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("json recieved is:", request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)