from django.shortcuts import render
from django.views import View
# from mixins.base import BaseOperationMixins
# from mixins.form import ModelFormMixin
# from mixins.response import ExtendedJsonResponse

# Create your views here.

class App(View):
    def get(self, request):
        return render(request, 'index.html')