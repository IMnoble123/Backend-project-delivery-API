from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Create your views here.
class ProductViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset         = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
