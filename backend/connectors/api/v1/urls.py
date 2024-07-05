from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136247ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136247", Testconnectors136247ViewSet, basename="testconnectors136247"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
