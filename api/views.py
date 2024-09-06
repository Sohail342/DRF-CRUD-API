from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# List and Retrieve Student (GET)
@api_view(['GET'])
def student_list(request, id=None):
    if id is not None:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# Create Student (POST)    
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Student (PUT/PATCH)
@api_view(['PUT', 'PATCH'])
def student_update(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, data=request.data, partial=True if request.method == 'PATCH' else False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Student (DELETE)
@api_view(['DELETE'])
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

