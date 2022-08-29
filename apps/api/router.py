from rest_framework.routers import DefaultRouter

from apps.category.views import (
    CategoryViewSet,
    SubCategoryViewSet
)

from apps.product.views import (
    ProductViewSet
)

from apps.accounts.views import (
    UserViewSet   
)


router = DefaultRouter()

router.register(r'user', UserViewSet,basename='user')
router.register(r'product', ProductViewSet,basename='product')
router.register(r'category', CategoryViewSet,basename='category')
router.register(r'sub-category', SubCategoryViewSet,basename='sub_category')
