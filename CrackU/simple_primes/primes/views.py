from django.shortcuts import render,redirect
from django.views import View

class input(View):
    def get(self, request):
        return render(request, 'input.html')

class output(View):
    def get(self, request):
        values=request.session.get('values')
        range1=request.session.get('range')
        request.session.pop('values',None)
        request.session.pop('range',None)
        return render(request, 'output.html',context={'values':values,'range':range1})   
    def post(self, request):
        range1=request.POST.get('range')
        values=[]
        for i in range(2,int(range1)+1):
            if self.checkPrime(i):  
                values.append(i)
        request.session['values']=values
        request.session['range']=range1
        return redirect('output')

    def checkPrime(self,val):
        for i in range(2,val//2+1):
            if val%i==0:
                return False
        return True
        