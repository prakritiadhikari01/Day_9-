from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student,Department
from .serializers import StudentSerializer,DepartmentSerializer
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                student = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method in ['PUT', 'PATCH', 'DELETE']:
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

        if request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
        elif request.method == 'PATCH':
            serializer = StudentSerializer(student, data=request.data, partial=True)
        elif request.method == 'DELETE':
            student.delete()
            return Response({'message': 'Student deleted successfully'}, status=204)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def department_api(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)