from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('origin/', views.OriginListView.as_view(), name = 'origin_list'),
    path('origin/<int:pk>/', views.OriginDetailView.as_view(), name = 'origin_detail'),
    path('review/', views.review_list, name='review_list'),
    path('review/<int:pk>/', views.review_detail, name='review_detail')
]
