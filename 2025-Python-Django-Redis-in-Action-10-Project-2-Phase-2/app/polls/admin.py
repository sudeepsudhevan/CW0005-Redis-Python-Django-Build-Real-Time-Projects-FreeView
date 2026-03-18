# polls/admin.py
from django.contrib import admin

from .models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("id", "question")  # Show these fields in admin list view
    search_fields = ("question",)  # Allow searching polls by question
