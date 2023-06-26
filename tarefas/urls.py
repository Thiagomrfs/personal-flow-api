from django.urls.conf import path
from .views import *

app_name = 'tarefas'

urlpatterns = [
    path('status', ListStatuses.as_view(), name='statuses'),
    path('categories', ListCategories.as_view(), name='categories'),
    path('<int:pk>', ViewTask.as_view(), name='view_task'),
    path('<int:pk>/comments', ViewTaskComments.as_view(), name='view_task_comments'),
]
