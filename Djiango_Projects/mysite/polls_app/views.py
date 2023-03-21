from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from polls_app.models import Question,Choice



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    ### the erro will be thrown when the entry is not queried correcly
    try:
        question = Question.objects.get(pk=question_id)
        print(question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #获取数据库的对象，如果无法获取到，抛出404错误，pk是primary key
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #操作数据库的数据+1
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #重定向，就是跳转到results界面
        #reverse函数可以借助 ulrs的name和参数 生成文本，例如 '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




def sayhi(request):
    return HttpResponse("sayhi")

