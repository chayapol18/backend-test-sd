from django_filters import FilterSet
from .models import SchoolModel, ClassroomModel, TeacherModel, StudentModel

class SchoolFilter(FilterSet):
    class Meta:
        model = SchoolModel
        fields = {
            'name': ['icontains']
        }

class ClassroomFilter(FilterSet):
    class Meta:
        model = ClassroomModel
        fields = {
            'school': ['exact'],
        }

class TeacherFilter(FilterSet):
    
    
    class Meta:
        model = TeacherModel
        fields = {
            'school': ['exact'],
            'classrooms': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'gender': ['exact'],
        }

class StudentFilter(FilterSet):
    class Meta:
        model = StudentModel
        fields = {
            'school': ['exact'],
            'classroom': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'gender': ['exact'],
        }