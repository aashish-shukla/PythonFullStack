from django.db import models

class Todo(models.Model):
    todo=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.todo
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Todos'
        verbose_name = 'Todo'
        db_table = 'todo'




