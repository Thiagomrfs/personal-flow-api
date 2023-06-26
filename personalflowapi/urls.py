from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import include, path
from .views import ListUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/', include("projetos.urls", namespace="projetos")),
    path('tasks/', include("tarefas.urls", namespace="tarefas")),
    path('users/', ListUsers.as_view(), name="list_users"),
]
