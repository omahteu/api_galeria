from .models import Imagem

from rest_framework import generics, permissions

from .serializers import FilaSerializer


class ImagemListCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagem.objects.all()
    serializer_class = FilaSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(token=self.request.user.auth_token.key)

    def get_queryset(self):
        return Imagem.objects.filter(token=self.request.user.auth_token.key)
