from django.shortcuts import render, redirect
from polls.models import Question, Choice, Select
from django.core.paginator import Paginator
import datetime, math


# Create your views here.
def index(request):
    return render(request, 'admin/index.html')

# 설문지 목록 최신순 출력
def poll_list(request):
    # 데이터 조회(시간 역순 정렬)
    polls = Question.objects.all().order_by('-created_at')
    # 페이징 처리
    paginator = Paginator(polls, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'polls' : polls,
        'page_obj' : page_obj,
    }
    return render(request, 'admin/poll_list.html', context)

# 특정 설문지 하나만 출력
def poll_detail(request, pk):
    poll = Question.objects.get(id=pk)
    choice = Choice.objects.filter(question_id=pk)
    print(choice)
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
        choice_name_data = request.POST.getlist('input[choice_name]')
        # select_name_data = request.POST.getlist('input[select_name]')
        # select_type_data = request.POST.getlist('input[select_type_name]')

        question_data = Question(question_text=question_name, created_at=datetime.datetime.now(),
                                 updated_at=datetime.datetime.now())
        print('1')
        print(question_data.pk)
        print(type(question_data))
        question_data.save()
        get_question = Question.objects.filter(question_text=question_name)
        print('2')
        print(get_question.pk)
        print(type(get_question.pk))
        # for element in choice_name_data:
        #     choice_data = Choice(question=Question.objects.get(id=get_question.id), choice_text=element)
        #     choice_data.save()

        # choice_data.save()
        # select_data.save()
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