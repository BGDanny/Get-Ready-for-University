from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('university/', views.UniversityListView.as_view(), name='university'),
    path('university/<str:pk>',
         views.UniversityDetailView.as_view(),
         name='university-detail'),
    path('professor/', views.ProfessorListView.as_view(), name='professor'),
    path('professor/<int:pk>',
         views.ProfessorDetailView.as_view(),
         name='professor-detail'),
    path('ranking/', views.RankingListView.as_view(), name='ranking'),
    path('ranking/<int:pk>',
         views.RankingDetailView.as_view(),
         name='ranking-detail'),
]
