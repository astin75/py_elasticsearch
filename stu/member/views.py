from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import memberData
import pandas as pd
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def memberList(request):
    member_List = memberData.objects.all()
    return render(request, 'member/memberList.html', {'member_List':member_List})

def memberUploadPage(request):
    return render(request, 'member/memberUpload.html')
@csrf_exempt
def memberUpload(request):
    name = request.POST['name']
    memberNumber = request.POST['memberNumber']
    age = request.POST['age']
    major = request.POST['major']

    qs = memberData(name=name, memberNumber=memberNumber, age=age, major=major)
    qs.save()
    return HttpResponseRedirect(reverse('member:memberList'))

def memberDownload(request):

    member_List = pd.DataFrame(list(memberData.objects.all().values()))
    member_List.to_csv("1.csv", index=False)
    return HttpResponseRedirect(reverse('member:memberList'))

@csrf_exempt
def memberFixed(request, name):

    memberNumber = request.POST['memberNumber']
    age = request.POST['age']
    major = request.POST['major']

    qs = memberData.objects.get(name=name)
    qs.memberNumber = memberNumber
    qs.age = age
    qs.major = major

    qs.save()
    return HttpResponseRedirect(reverse('member:memberList'))

@csrf_exempt
def memberFixedPage(request, name):
    qs = memberData.objects.get(name=name)
    context = {
        'mode' : 'fixed',
        'memberInfo' : qs}

    return render(request, 'member/memberDetail.html', context)

@csrf_exempt
def memberDelete(request, name):
    qs = memberData.objects.get(name=name)
    qs.delete()

    return HttpResponseRedirect(reverse('member:memberList'))


