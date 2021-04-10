from django.contrib import admin
from .models import *
from .forms import *

@admin.register(ToDo)


class ToDoPanel(admin.ModelAdmin):
  list_filter = ['user', 'title', 'complete', 'created', 'last_date']
  list_display = ['user', 'title', 'complete', 'created', 'last_date']
  list_display_links = ['user', 'title', 'complete', 'created', 'last_date']
  search_fields = ['user']
  list_filter = ['user']

  class Meta:
    model = ToDo

