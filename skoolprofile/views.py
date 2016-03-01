from django.shortcuts import render
from .models import school
from .models import timezone

# Create your views here.
def school_list(request):
    schools= school.objects.order_by('name')
    return render(request,'skoolprofile/school_list.html',{'schools':schools})