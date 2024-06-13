from django.db import models

class SchoolModel(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
class ClassroomModel(models.Model):
    grade = models.IntegerField()
    section = models.IntegerField()
    school = models.ForeignKey(SchoolModel, related_name='classrooms', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.grade}/{self.section}"
    
class TeacherModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.ForeignKey(SchoolModel, related_name='teachers', on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(ClassroomModel, related_name='teachers')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}"
    
class StudentModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.ForeignKey(SchoolModel, related_name='students', on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassroomModel, related_name='students', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}"