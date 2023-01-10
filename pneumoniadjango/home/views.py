from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import os

#import test
# Create your views here.
 
 
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            #os.system('cmd/c "conda activate tf"')
            import test
            return render(request, 'result.html',{'output':test.result})
            
          #  return HttpResponse('successfully uploaded')
            #return redirect('success')
    else:
        form = Form()
    return render(request, 'index.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')