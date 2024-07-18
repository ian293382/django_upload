from django.urls import path
from . import views

#  使用 re_path 可以讓路由更靈活 但是  path('get_author_courses/<int:user_id>/' 這樣可以更直觀
app_name = 'demo'
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),

]