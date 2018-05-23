from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiaryListView.as_view()),
    path('diary/create/', views.DiaryCreate.as_view()),  
    path('diary/<int:pk>/update/', views.DiaryUpdate.as_view()),
    path('diary/<int:pk>/delete/', views.DiaryDelete.as_view()), 
    path('money', views.MoneyListView.as_view()),
    path('money/create/', views.MoneyCreate.as_view()),
    path('money/<int:pk>/update/', views.MoneyUpdate.as_view()),
    path('money/<int:pk>/delete/', views.MoneyDelete.as_view()),    
]