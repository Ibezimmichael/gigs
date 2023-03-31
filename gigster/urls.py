from django.urls import path
from .views import GigListView, GigCreateView, GigUpdateView, GigDeleteView, GigDetailView

urlpatterns = [
    path('', GigListView.as_view(), name='gig_list'),
    path('create/', GigCreateView.as_view(), name='gig_create'),
    path('<int:pk>/update/', GigUpdateView.as_view(), name='gig_update'),
    path('<int:pk>/delete/', GigDeleteView.as_view(), name='gig_delete'),
    path('<int:pk>/', GigDetailView.as_view(), name='gig_detail'),
]
