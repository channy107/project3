from django.http import HttpResponse
from django.shortcuts import render

def upload1(request):
    if request.method == 'GET':
        return render(request, 'file/upload1.html',{})
    else:
        upload_file1 = request.FILES['my_file1']
        upload_file2 = request.FILES['my_file2']
        return HttpResponse('완료'+ upload_file1.name)

def upload2(request):
    if request.method == 'GET':
        return render(request, 'file/upload2.html',{})
    else:
        upload_files = request.FILES.getlist('my_file')
        for upload_file in upload_files:
            print(upload_file.name)


        return HttpResponse('완료'+ upload_file.name)