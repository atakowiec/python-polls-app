from django.contrib import admin
from polls.models import Poll, Option


class OptionInline(admin.TabularInline):
    """
    Inline representation for options within the Poll admin page.
    """
    model = Option
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Poll model.
    """
    list_display = ("title", "is_active", "created_at")
    inlines = [OptionInline]
