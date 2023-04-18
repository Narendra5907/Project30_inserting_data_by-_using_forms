from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic name entered successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        TO=Topic.objects.get(topic_name=topic)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('Webpage insertion is done Successfully')


    return render(request,'insert_webpage.html',d)

def insert_AcessRecord(request):
    LTO=Webpage.objects.all()
    d={'webpages':LTO}

    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(name=name)
        AO=AcessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('Webpage insertion is done Successfully')

    return render(request,'insert_AcessRecord.html',d)


def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)

       
        return HttpResponse('retrieve data  Successfully')
    return render(request,'retrieve_data.html',d)


def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)


def radiobutton(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'radiobutton.html',d)

def update_topic(request):
    LTO=Webpage.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        new=request.POST['new']
        print(tn)
        print(new)
        for i in tn:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)

       
        return HttpResponse('retrieve data  Successfully')
    return render(request,'retrieve_data.html',d)

    LTO=Webpage.objects.all()
    d={topic}