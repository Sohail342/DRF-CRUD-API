from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer

# Display all objects (records or Rows) from Student table  
def students_api(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)

# Display particular object (record or Row) from Student table  
def student_api(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data, safe=False)