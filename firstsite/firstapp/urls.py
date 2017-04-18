from  django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^index/', views.index,name='index'),
    url(r'^article_page/(?P<aritcle_id>[0-9]+)$', views.aritcle_page,name='aritcle_page'),
    # url(r'^article_page/', views.article_page,name='article_page'),
    url(r'^edit/', views.edit_page,name='edit_page'),
    url(r'^edit/action', views.edit_action,name='edit_action'),
]