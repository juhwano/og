from django.shortcuts import render, redirect
from polls.models import Question, Choice
import datetime
import json
from django.http import JsonResponse
from django.views import View
# Create your views here.
def index(request):
    return render(request, 'admin/index.html')

# 설문지 목록 최신순 출력
def poll_list(request):
    polls = Question.objects.all().order_by('-created_at')
    context = {
        'polls' : polls
    }
    return render(request, 'admin/poll_list.html', context)

# 특정 설문지 하나만 출력
def poll_detail(request, pk):
    poll = Question.objects.get(id=pk)
    choice = Choice.objects.filter(question_id=pk)
    context = {
        'poll' : poll,
        'choice' : choice,
    }
    return render(request, 'admin/poll_detail.html', context)

# 설문지 생성 페이지로 이동
def poll_create(request):
    return render(request, 'admin/poll_create.html')

# 설문지 생성 DB 작업
def new_poll(request):
    if request.method == 'POST':
        question_name = request.POST.get('question_name')
        question_count = request.POST.get('question_count')
        question_status = request.POST.get('question_status')
        choice_name = request.POST.getlist('choice_name')
        print(choice_name)

        question_data = Question(question_text= question_name, count=question_count, status=question_status, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
        choice_data = Choice(choice_text=choice_name) # id는 어떻게?

        question_data.save()
        choice_data.save()
        return redirect('/admin/polls')

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