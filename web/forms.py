from django import forms
from .models import Diary, Money

class DiaryForm(forms.ModelForm):
  class Meta:
    model = Diary
    fields = ['memo']
    widgets = {
      'memo': forms.Textarea(attrs={'class': 'form-control'}),
    }

class MoneyForm(forms.ModelForm):
  class Meta:
    model = Money
    fields = '__all__'
    widgets = {
      'item': forms.TextInput(attrs={'class': 'form-control'}),
      'kind': forms.Select(attrs={'class': 'form-control'}),
      'price': forms.NumberInput(attrs={'class': 'form-control'}),
    }