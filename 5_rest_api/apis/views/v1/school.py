from rest_framework import viewsets
from ...models import SchoolModel
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter