from django.shortcuts import render
from django.http import HttpResponse
from .form import InputForm
from .tweetChek import checkTweet



def index(request):
    params = {
        'form':InputForm(),
        'text': ""
    }

    return render(request, 'app/index.html',params)

def check(request):
    params = {
        'text':None,
        'result':None
    }
    if request.method == 'POST':
        formText = InputForm(request.POST)
        if formText.is_valid():
            params['text'] = formText.cleaned_data['text']
    params['result'] = checkTweet(params['text'])
    return render(request, 'app/base.html',params)