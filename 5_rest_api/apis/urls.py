from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1 import school, classroom, student, teacher

router = DefaultRouter()
router.register('school', school.SchoolViewSet)
router.register('classroom', classroom.ClassroomViewSet)
router.register('teacher', teacher.TeacherViewSet)
router.register('student', student.StudentViewSet)

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls)),
]
