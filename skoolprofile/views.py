from django.shortcuts import render

# Create your views here.
def school_list(request):
    return render(request,'skoolprofile/school_list.html',{})