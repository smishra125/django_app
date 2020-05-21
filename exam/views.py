from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showTest(request):
    # res = render(request, 'exam/test.html')
    # return res
    que = "Who developed C Language?"
    a = "Ken Thompson"
    b = "Dennis Ritchie"
    c = "Bjarne Stroustrup"
    d = "Shubham Mishra"
    data = {'que': que, 'a': a,'b': b, 'c': c, 'd': d}
    res = render(request, 'exam/test.html', context=data)
    return res

def showResult(request):
    s="<h1>This is show exam Result Page</h1>"
    return HttpResponse(s)

def about(request):
    return render(request, 'exam/about.html')

def message(request):
    msg = "This is a message page"
    return render(request, 'exam/tags.html', {'msg':msg})