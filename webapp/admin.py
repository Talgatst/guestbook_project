from django.contrib import admin
from webapp.models import GuestBookReview


@admin.register(GuestBookReview)
class GuestBookReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'text')
