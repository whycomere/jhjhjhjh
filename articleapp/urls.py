from django.urls import path
from django.views.generic import TemplateView #템플릿을 보여주는가ㅓ

from articleapp.views import ArticleCreateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),

]

