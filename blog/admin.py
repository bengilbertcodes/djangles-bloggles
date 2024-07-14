from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customises the admin interface for the Post model.

    This class inherits from SummernoteModelAdmin to include rich text 
    editing capabilities for specified fields. It provides various 
    configurations to enhance the admin interface for managing Post 
    instances.

    Attributes:
        list_display (tuple): Specifies the fields to display in the list 
                              view of the admin interface. Displays 'title', 
                              'slug', 'status', and 'created_on'.
        search_fields (list): Defines the fields to include in the search 
                              functionality. Searches can be performed on 
                              'title' and 'content'.
        list_filter (tuple): Adds filters in the admin list view for 
                             'status' and 'created_on'.
        prepopulated_fields (dict): Automatically populates the 'slug' 
                                    field based on the 'title' field.
        summernote_fields (tuple): Specifies the fields that should use 
                                   the Summernote rich text editor. 
                                   In this case, it applies to 'content'.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug':('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)