from django.urls import path
from . import views

app_name ='admin'

urlpatterns = [
    path('', views.index, name='index'),
    # 설문지 목록 보기(admin)
    path('polls/', views.poll_list, name='list'),
    # 설문지 상세 보기(admin/5)
    path('polls/<int:pk>', views.poll_detail, name='detail'),
    # 설문지 생성(admin/create)
    path('polls/create/', views.poll_create, name='create'),
    # 설문지 수정(admin/5/update)
    path('polls/<int:pk>/update', views.poll_update, name='update'),
    # 설문지 삭제(admin/delete)
    path('polls/<int:pk>/delete', views.poll_delete, name='delete'),
    # 설문지 분석(admin/a)
    path('a/', views.poll_analysis, name='analysis'),
]