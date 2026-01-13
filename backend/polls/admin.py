from django.contrib import admin
from polls.models import Poll, Option


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    inlines = [OptionInline]
