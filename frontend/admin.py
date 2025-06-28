
from django.contrib import admin
from .models import CreateTodoModel

class CreateTodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'isCompleted', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('isCompleted', 'created_at', 'updated_at')
    
    class Meta:
        varbose_plural_name = 'Create To Do'
    
admin.site.register(CreateTodoModel, CreateTodoAdmin)