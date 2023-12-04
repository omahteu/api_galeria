from django.db import models

from datetime import datetime

agora = str(datetime.now().strftime("%M%S_%f"))


def subir_imagem(token, filename):
    return f"{agora}-{filename}"


class Imagem(models.Model):
    token = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to=subir_imagem)
    titulo = models.CharField(max_length=50)
    comentario = models.TextField()
    estado = models.CharField(max_length=10, blank=True)
    curtida = models.CharField(max_length=5)
