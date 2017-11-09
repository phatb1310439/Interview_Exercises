from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Question    
from django.http import Http404

#part 2
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#..................................    Raising a 404 error
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist ")
#     return render(request, 'polls/detail.html', {'question': question})

#........A shortcut: get_object_or_404()
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})





def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
#..............................part 1
# def index(request):

#     response = HttpResponse()
#     response.writelines("<h1>HELLO DJANGO<h1>")
#     response.writelines("<h2>My name's Phat<h2>")
#     response.writelines("<h3>You're at the polls index<h3>")
#     return response
#................................
#........................part 3
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

#........................part 4
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#........................part 5 A shortcut: render()
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)