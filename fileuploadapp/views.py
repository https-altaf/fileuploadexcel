from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import uploadfile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
         
            file = form.cleaned_data['file']
            uploadfile.objects.create(file=file)
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'success.html')
