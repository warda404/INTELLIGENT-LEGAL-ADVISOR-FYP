from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='law-home'),
    path('login/', views.login, name='law-login'),
    path('lawyer_data/', views.show_lawyers, name='lawyer-list'),
    path('verdict/', views.predict_verdict,
         name='law-verdict-prediction'),
    path('document_similarity/', views.document_similarity,
         name='document-similarity'),
    path('summarize/', views.summarize, name='law-summarize'),
    path('case_to_section/', views.case_to_section,
         name='law-case-to-section'),

]
