from datetime import datetime
from random import randint

from django.db.models import Max, Min, Avg
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice, QuizMarks

# Create your views here.

from django.http import HttpResponse

question_list = []
def start(request):
    ques_num_list = generateFiveRand(20)
    global question_list
    question_list = []
    for i in ques_num_list:
        question_list.append(get_object_or_404(Question, pk=i))
    context = {'question_list': question_list}
    return render(request, 'quiz/start.html', context)
    #detail(request, 1, ques_num_list)

def results(request):
    correct = 0
    global question_list
    for i in range (0,5):
        print('choice'+str(i+1))
        print(request.POST['choice'+str(i+1)])
        print(question_list[i].choice_set.all())
        selected_choice = question_list[i].choice_set.get(pk=request.POST['choice'+str(i+1)])
        if(selected_choice.isCorrect):
            correct+=1
    quizmarks = QuizMarks()
    quizmarks.user = request.user
    quizmarks.marks = correct
    quizmarks.pub_date = datetime.now()
    quizmarks.save()
    context = {
        'correct': correct,
        'total': 5,
        'percentage': correct*100/5
    }
    return render(request, 'quiz/results.html', context)

def generateFiveRand(limit):
    ques_set = set()
    while(len(ques_set) < 5):
        value = randint(1, limit)
        ques_set.add(value)
    return list(ques_set)

def statistics(request):
    max_marks = QuizMarks.objects.all().aggregate(Max('marks'))
    min_marks = QuizMarks.objects.all().aggregate(Min('marks'))
    average_marks = QuizMarks.objects.all().aggregate(Avg('marks'))
    average = 0
    max = 0
    min = 0
    if max_marks['marks__max'] is not None:
        max = max_marks['marks__max']
    if min_marks['marks__min'] is not None:
        min = min_marks['marks__min']
    if average_marks['marks__avg'] is not None:
        average = round(average_marks['marks__avg'],2)
    user_quiz_history = QuizMarks.objects.filter(user = request.user)
    context = {
        'max': max,
        'min': min,
        'avg': average,
        'total': 5,
        'user_quiz_history': user_quiz_history
    }
    return render(request, 'quiz/statistics.html', context)
