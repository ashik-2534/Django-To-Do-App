from django.db import models


class CreateTodoModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Create To Do"

    def __str__(self):
        return self.title
