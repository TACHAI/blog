from django.shortcuts import render,HttpResponse
import firstapp.models
from django.template import Context,Template
# Create your views here.
from firstapp.models import *

# from firstapp.models import People, Aritcle
from . import models


def first_try(request):
    # request可以改用别的
    person=People(name='hu',job='officer')
    # 模板
    html_string='''
    <html>
        <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
        </head>
        <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ person.name }}
                </h1>
        </body>
    </html>

    '''
    t=Template(html_string)
    c=Context({'person':person})
    web_page=t.render(c)
    # 渲染
    return HttpResponse(web_page)
def index(request):
     context={}
     aritcle_list=models.Aritcle.objects.all()
     context['aritcle_list']=aritcle_list
     index_page=render(request,'first_web_2.html',context)
     # render第三个参数是后台传送到前端的数据
     return index_page
def aritcle_page(request,aritcle_id):
    context={}
    # aritcle=Aritcle.objects.all()
    aritcle=models.Aritcle.objects.get(pk=aritcle_id)
    context['aritcle']=aritcle
    return render(request,'aritcle_page.html',context)
def edit_page(request):
    return render(request,'edit_page.html')
def edit_action(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    models.Aritcle.objects.create(title=title,content=content)
    # 返回首页
    aritcle_list =models.Aritcle.objects.all()
    content['aritcle_list'] = aritcle_list
    index_page = render(request, 'first_web_2.html', content)
    return index_page