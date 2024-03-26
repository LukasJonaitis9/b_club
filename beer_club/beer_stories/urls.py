from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
<<<<<<< Updated upstream
    path('origin/', views.OriginListView.as_view(), name = 'origin_list'),
    path('origin/<int:pk>/', views.OriginDetailView.as_view(), name = 'origin_detail'),
=======
    path('type/', views.TypeListView.as_view(), name = 'type_list'),
    path('type/<int:pk>/', views.TypeDetailView.as_view(), name='type_detail'),
    path('type/create', views.TypeCreateView.as_view(), name='type_create'),
>>>>>>> Stashed changes
    path('review/', views.review_list, name='review_list'),
    path('review/<int:pk>/', views.review_detail, name='review_detail')
]