from django.urls.conf import path
from .views import *

app_name = 'projetos'

urlpatterns = [
    path('', ViewProjects.as_view(), name='view_projects'),
    path('<int:pk>', ViewProject.as_view(), name='view_project'),
    path('<int:pk>/tasks', ViewProjectTasks.as_view(), name='view_project'),
]