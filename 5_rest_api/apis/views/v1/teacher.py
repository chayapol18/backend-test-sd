from rest_framework import viewsets
from ...models import TeacherModel
from ...serializers import TeacherSerializer, TeacherCreateUpdateSerializer
from ...filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TeacherCreateUpdateSerializer
        else:
            return TeacherSerializer