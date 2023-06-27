# file_upload/views.py
from django.shortcuts import render

def index(request):
    file_contents = []

    if request.method == 'POST' and request.FILES.getlist('files'):
        files = request.FILES.getlist('files')
        for file in files:
            file_content = file.read().decode('utf-8')
            file_contents.append(file_content)

    return render(request, 'home.html', {'file_contents': file_contents})
