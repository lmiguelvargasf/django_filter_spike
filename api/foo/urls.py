from foo.models.author import Author
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

router = DefaultRouter()
router.register(f'authors', AuthorViewSet)

urlpatterns = router.urls
