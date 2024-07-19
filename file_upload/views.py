from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
import os 
import uuid 
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat

def file_list(request):
    files = File.objects.all().order_by('-id')
    return render(request, 'file_list.html',{ 'files': files})

# Regular file upload without using ModelForm 徒手打造用os.path 來幹這件事情
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            raw_file = form.cleaned_data.get('file')
            upload_method = form.cleaned_data.get('upload_method')
            new_file = File()
            new_file.file = handle_upload_file(raw_file)
            new_file.upload_method = upload_method
            new_file.save()
            return redirect('file_upload:file_list')  # 使用命名空間
    else:
        form = FileUploadForm()

    return render(request, 'upload_form.html', {
        'form': form,
        'handling': 'Upload files with Regular form'
    })



def view_file(request, pk):
    file_instance = get_object_or_404(File, pk=pk)
    return render(request, 'view_file.html', {'file': file_instance})

def handle_upload_file(file):
    # 查看最後檔案格式 pdf png ....
    ext = file.name.split('.')[-1] 
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path

# handle_upload_file 後面必須要包media 否則就是相對地址
# 建議一定要寫入絕對路徑時必須要用os.path.exists 檢查是否存在 

# ModelForm 處理文件上傳 可以跟 file_upload做比較 後續會有ajax 依然可以比對
def model_form_upload(request):
    if request.method == 'POST':
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # 正常我們使用form model
            return redirect('/file/file')
    else:
        form = FileUploadModelForm() # 給空的讓使用者填寫
    return render( request, 'upload_form.html',
                    {'form': form,
                     'heading': 'Upload files with ModelForm'
                     }
                  )