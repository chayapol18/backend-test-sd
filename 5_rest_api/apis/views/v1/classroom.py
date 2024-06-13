from rest_framework import viewsets
from ...models import ClassroomModel
from ...serializers import ClassroomSerializer, ClassroomCreateUpdateSerializer
from ...filters import ClassroomFilter

# {"first_name":"test", "last_name": "last", "gender": "male"}
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = ClassroomModel.objects.all()
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ClassroomCreateUpdateSerializer
        else:
            return ClassroomSerializer