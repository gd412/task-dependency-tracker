from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet, TaskDependencyViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'dependencies', TaskDependencyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
