from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', views.CustomUserViewSet, basename="user")
router.register(r'posts', views.PostViewSet, basename="post")

urlpatterns = router.urls
