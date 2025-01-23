

# Register your models here.
from django.contrib import admin
from .models import StudyRecord

@admin.register(StudyRecord)
class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'hours_studied')  # Display user and hours studied in the admin list view
    search_fields = ('user__username',)      # Add a search bar to search by username
