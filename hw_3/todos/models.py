
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=2000, blank=True, default='')
    due_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f'ID: {self.id} {self.title}'

