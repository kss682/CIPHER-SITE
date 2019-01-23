from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Encrypt
# Create your views here.
class LandingPage(TemplateView):
    template_name = 'base.html'

    def encrypt(self,string,key):
        Estring = ""
        for value in string:
            if ord(value) in range(97,123):
                Estring += chr((ord(value)-94)%26 + 94 + key)
            elif ord(value) in range(65,91):
                Estring += chr((ord(value)-62)%26 + 62 + key)
            else:
                Estring += value
        print(Estring)
        return Estring

    def get(self, request):
        form    =   Encrypt()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form =  Encrypt(request.POST)
        if form.is_valid():
            text = form.cleaned_data['Etext']
            print(text)
            key  = form.cleaned_data['Ekey']
            text = self.encrypt(text,key)
            print(text)
            arg = {'form':form,'data':text}
        else:
                print(form.errors)

        return render(request,self.template_name,arg)
