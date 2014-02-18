from django.contrib import admin
from demo.models import Todo

# Let Django Admin can edit 
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)
                                                                                                 
admin.site.register(Todo, TodoAdmin)