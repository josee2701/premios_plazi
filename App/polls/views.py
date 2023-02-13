from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.all()
    return render (request, "polls/index.html", {"latest_question_list":latest_question_list})


def detail(request, question_id):
    question= get_object_or_404(Question, pk =question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    question= get_object_or_404(Question, pk =question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {"question": question,
                                                     "error_message":"No eliste una respuesta"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
