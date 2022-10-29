from rest_framework import viewsets,permissions
from .serializers import UsersSerializers
from .models import Users

#* crea los metdos => GET,POST,PUT,DELETE por defecto
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializers