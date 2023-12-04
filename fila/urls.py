from django.urls import path

from .views import ImagemListCreateView

urlpatterns = [
    path('upload/', ImagemListCreateView.as_view(), name='upload_imagem'),
]
