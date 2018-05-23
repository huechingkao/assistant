from django.shortcuts import render
from django.views import generic
from .models import Diary
from .models import Money
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class DiaryListView(generic.ListView):
    model = Diary
    ordering = ['-id']
    paginate_by = 3  

@method_decorator(login_required, name='dispatch')    
class DiaryCreate(CreateView):
    model = Diary
    fields = ['memo']
    success_url = "/"   
    template_name = 'form.html'   

@method_decorator(login_required, name='dispatch')    
class DiaryUpdate(UpdateView):
    model = Diary
    fields = '__all__'   
    success_url = "/"   
    template_name = 'form.html'    

@method_decorator(login_required, name='dispatch')    
class DiaryDelete(DeleteView):
    model = Diary
    success_url = "/"
    template_name = 'confirm_delete.html' 

@method_decorator(login_required, name='dispatch')        
class MoneyListView(generic.ListView):
    model = Money
    ordering = ['-id']
    paginate_by = 3  

@method_decorator(login_required, name='dispatch')    
class MoneyCreate(CreateView):
    model = Money
    fields = '__all__'
    success_url = "/web/money"
    template_name = 'form.html'

@method_decorator(login_required, name='dispatch')    
class MoneyUpdate(UpdateView):
    model = Money
    fields = '__all__'
    success_url = "/web/money"    
    template_name = 'form.html'      

@method_decorator(login_required, name='dispatch')    
class MoneyDelete(DeleteView):
    model = Money
    success_url = "/web/money"   
    template_name = 'confirm_delete.html'           