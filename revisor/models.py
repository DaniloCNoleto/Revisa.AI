# Em: revisor/models.py

from django.db import models
from django.contrib.auth.models import User

class QueueEntry(models.Model):
    # --- DEFINIÇÃO DOS CHOICES PARA O CAMPO STATUS ---
    STATUS_CHOICES = [
        ('na_fila', 'Na Fila'),
        ('processando', 'Processando'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
        ('erro', 'Erro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=512, default='')
    
    # --- CAMPO STATUS ATUALIZADO PARA USAR CHOICES ---
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='na_fila')
    
    progress = models.IntegerField(default=0)
    mode = models.CharField(max_length=50, default='completa')
    
    output_file_url = models.CharField(max_length=512, null=True, blank=True)
    duration_seconds = models.FloatField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.file_name} por {self.user.username} - {self.status} ({self.progress}%)"