from django.urls import path
from . import views

app_name = 'file_upload' 

urlpatterns = [
    path('upload_files/', views.file_upload, name='upload_file'),
    path('view_file/<int:pk>/', views.view_file, name='view_file'),  # 用於文件查看或操作，需要 pk
    path('upload_form_model/', views.model_form_upload, name='model_form_upload'), # FileUploadForm
    path('file/', views.file_list, name='file_list'),

]