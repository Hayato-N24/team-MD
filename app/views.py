from django.shortcuts import render
from django.http import HttpResponse
from .form import InputForm
import pickle



def index(request):
    params = {
        'form':InputForm(),
        'text': ""
    }

    return render(request, 'app/index.html',params)

def test(request):
    params = {
        'text': ""
    }
    if request.method == 'POST':
        formText = InputForm(request.POST)
        if formText.is_valid():
            params['text'] = formText.cleaned_data['text']
    return HttpResponse(params['text'])