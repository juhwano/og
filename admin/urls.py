from django.urls import path
from . import views

app_name ='admin'

urlpatterns = [
    # 관리자 메인 페이지
    path('', views.index, name='index'),
    # 설문지 목록 보기
    path('polls/', views.poll_list, name='list'),
    # 설문지 상세 보기
    path('polls/<int:pk>', views.poll_detail, name='detail'),
    # 설문지 생성 페이지
    path('polls/create/', views.poll_create, name='create'),
    # 설문지 생성 데이터 저장
    path('polls/new/', views.new_poll, name='new'),
    # 설문지 수정
    path('polls/<int:pk>/update', views.poll_update, name='update'),
    # 설문지 삭제
    path('polls/<int:pk>/delete', views.poll_delete, name='delete'),
    # 관리자 분석 페이지
    path('a/', views.poll_analysis, name='analysis'),
]