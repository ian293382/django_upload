# 定義一個表單FileUploadForm 並使用 Clean方法 對用戶上傳的文件做驗證
from django import forms
from .models import File

class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    upload_method =  forms.CharField(label='Upload Method', max_length=20,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_file(self):
        file = self.cleaned_data.get('file')
        ext =  file.name.split('.')[-1].lower() # 驗證檔案名稱 txt jpg...
        if ext not in ['jpg','pdf', 'xlsx']:
            raise forms.ValidationError('Only jpg, pdf and xlsx file are allowed')
        # 驗定要 return 驗證過後的數據 只有在view中才能夠使用 form.cleaned_data.get('xxx') 才能獲取驗證後的數據
        return file