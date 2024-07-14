from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Confirguration for the 'about' app.

    Attributes:
        default_auto_field (str): Specifies the type of auto-incrementing 
            primary key field to use in the app. Defaults to 
            'django.db.models.BigAutoField'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
