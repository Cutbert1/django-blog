from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    AppConfig class for the 'blog' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
