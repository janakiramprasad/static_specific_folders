from django.shortcuts import render

# Create your views here.
def specific_static_folders(request):
    return render(request,'specific_static_folders.html')