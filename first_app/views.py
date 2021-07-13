from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def index_test(request):
    return tpResponse('Hello world!!!!!')

class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello World!!!@###")
