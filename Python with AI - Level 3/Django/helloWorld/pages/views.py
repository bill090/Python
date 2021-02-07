from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("""<h1>Hello World! - William
    <a href="http://127.0.0.1:8000/simple/">Visit the simpler version here.</a></h1>""")
def simplePageView(request):
    return HttpResponse("""<p>Hello World! - William
    <a href="http://127.0.0.1:8000/">Go back to the original version here.</a><p>""")