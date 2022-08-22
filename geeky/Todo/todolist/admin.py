from django.contrib import admin
from todolist.models import Todo, ToDoAdmin

# Register your models here.
#admin.site.register((Todo))
admin.site.register(Todo, ToDoAdmin)