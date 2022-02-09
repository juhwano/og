from django.shortcuts import render, redirect
from polls.models import Question, Choice
import datetime
import json
from django.http import JsonResponse
from django.views import View
# Create your views here.
def index(request):
    return render(request, 'admin/index.html')

def poll_list(request):
    # 진행중인 설문지 목록 최신순 출력
    polls = Question.objects.all().order_by('-created_at')
    return render(request, 'admin/poll_list.html', {'polls' : polls})

def poll_detail(request):
    pass

def poll_create(request):
    # 설문지 생성
    if request.method == 'POST':
        poll_data = request.POST

        data = Question(question_text= poll_data.get('poll_name'), choice_count=poll_data.get('choice_count'), status=poll_data.get('status'), created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
        data.save()
        return redirect('/admin/')

def poll_update(request, pk):
    if request.method == 'POST':
        poll_data = request.POST
        my_poll = Question.objects.get(id=pk)
        my_poll.updated_at = datetime.datetime.now()
        my_poll.question_text = poll_data.get('question_text')
        my_poll.choice_count = poll_data.get('question_text')
        my_poll.choice_status = poll_data.get('status')
        my_poll.save()
        return redirect(f'/admin/{pk}')

def poll_delete(request, pk):
    poll = Question.objects.get(id=pk)
    poll.delete()
    return redirect('/admin/')

def poll_analysis(request):
    return render(request, 'admin/poll_analysis.html')