from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import (
    AutorSerializer,
    CategoriaSerializer,
    EditoraSerializer,
    LivroDetailSerializer,
    LivroSerializer,
)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer