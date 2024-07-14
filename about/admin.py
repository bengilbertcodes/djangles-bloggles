from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Customises the admin interface for the About model.

    This class inherits from SummernoteModelAdmin to include rich text 
    editing capabilities for specified fields. It provides a configuration 
    to enhance the admin interface for managing About instances.
    """
    summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Customises the admin interface for the CollaborateRequest model.

    This class inherits from admin.ModelAdmin and provides configurations 
    to enhance the admin interface for managing CollaborateRequest instances.
    """
    list_display = ('message', 'read',)