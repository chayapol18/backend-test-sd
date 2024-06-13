from rest_framework import viewsets
from ...models import StudentModel
from ...serializers import StudentSerializer, StudentCreateUpdateSerializer
from ...filters import StudentFilter

# {"first_name":"test", "last_name": "last", "gender": "male"}
class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return StudentCreateUpdateSerializer
        else:
            return StudentSerializer