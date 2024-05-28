from django.urls import path
from .views import AvaliacaoListView, AvaliacaoCreateView, AvaliacaoUpdateView, AvaliacaoDetailView, AvaliacaoDeleteView

app_name = 'avaliacao'

urlpatterns = [
    path('', AvaliacaoListView.as_view(), name='avaliacao-list'),
    path('create/', AvaliacaoCreateView.as_view(), name='avaliacao-create'),
    path('<int:pk>/', AvaliacaoDetailView.as_view(), name='avaliacao-detail'),
    path('<int:pk>/update/', AvaliacaoUpdateView.as_view(), name='avaliacao-update'),
    path('<int:pk>/delete/', AvaliacaoDeleteView.as_view(), name='avaliacao-delete'),
]
