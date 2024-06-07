from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models import employee
from myapp.serializer import employee_serializer


# Create your views here.

class employee_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        employee_object = employee.objects.all()
        serializer = employee_serializer(employee_object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = employee_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class employee_list_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return employee.objects.get(pk=pk)
        except employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        emp_obj = self.get_object(pk)
        serializer = employee_serializer(emp_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        emp_obj = self.get_object(pk)
        serializer = employee_serializer(emp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class employee_list_generic_view(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employee_serializer


class employee_list_generic_view_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employee_serializer
