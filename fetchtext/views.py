from django.shortcuts import render
from .models import FilesUpload

def show_error():
    error = {}
    error['emptyData'] = "Something went wrong"
    return error

def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        ################ [1] Save input image to database ##############
        document = FilesUpload.objects.create(file=file2)
        document.save()
        return render(request, "error.html", {'error' : show_error()})
    return render(request, "index.html")