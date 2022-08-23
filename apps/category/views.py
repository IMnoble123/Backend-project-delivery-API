from .models import Category,SubCategory
from .serializers import CategorySerializer,SubCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Create your views here.
class CategoryViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = SubCategory.objects.all().order_by('id')
    serializer_class = SubCategorySerializer
