from rest_framework import serializers
from .models import SchoolModel, ClassroomModel, TeacherModel, StudentModel

class SchoolSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()
    
    class Meta:
        model = SchoolModel
        fields = '__all__'  
    
    def get_classrooms_count(self, obj):
        return obj.classrooms.count()

    def get_teachers_count(self, obj):
        return obj.teachers.count()

    def get_students_count(self, obj):
        return obj.students.count()
    
class TeacherCreateUpdateSerializer(serializers.ModelSerializer):
    classrooms = serializers.PrimaryKeyRelatedField(many=True, queryset=ClassroomModel.objects.all())
    class Meta:
        model = TeacherModel
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    classrooms = serializers.StringRelatedField(many=True)
    school = serializers.StringRelatedField()
    class Meta:
        model = TeacherModel
        fields = '__all__'

class StudentCreateUpdateSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(many=False, queryset=ClassroomModel.objects.all())
    class Meta:
        model = StudentModel
        fields = '__all__'
    
class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField()
    school = serializers.StringRelatedField()
    class Meta:
        model = StudentModel
        fields = '__all__'
    
class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=StudentModel.objects.all())
    teachers = serializers.PrimaryKeyRelatedField(many=True, queryset=TeacherModel.objects.all())
    
    class Meta:
        model = ClassroomModel
        fields = '__all__'
    
class ClassroomSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    students = StudentSerializer(many=True)
    # students = serializers.SerializerMethodField()
    # teachers = serializers.SerializerMethodField()
    
    class Meta:
        model = ClassroomModel
        fields = '__all__'

    # def get_students(self, obj):
    #     return serializers.StringRelatedField(many=True).to_representation(obj.students.all())
    
    # def get_teachers(self, obj):
    #     return serializers.StringRelatedField(many=True).to_representation(obj.teachers.all())