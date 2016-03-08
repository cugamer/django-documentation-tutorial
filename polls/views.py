from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	# This can be done by getting the template, then returning the response
	# with the template and passing the context to the template
	# template = loader.get_template('polls/index.html')
	# return HttpResponse(template.render(context, request))

	# This is the shortcutwhich uses the render method.
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# return HttpResponse("You're looking at question %s." % question_id)
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)