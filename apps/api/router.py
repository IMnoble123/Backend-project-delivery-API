from rest_framework.routers import DefaultRouter

from apps.category.views import (
    CategoryViewSet,
    SubCategoryViewSet
)

from apps.product.views import (
    ProductViewSet
)

router = DefaultRouter()

router.register(r'product', ProductViewSet,basename='product')
router.register(r'category', CategoryViewSet,basename='category')
router.register(r'sub-category', SubCategoryViewSet,basename='sub_category')
