from foo.models.author import Author
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, PublisherViewSet

router = DefaultRouter()
router.register(f'authors', AuthorViewSet)
router.register(f'books', BookViewSet)
router.register(f'publishers', PublisherViewSet)

urlpatterns = router.urls
