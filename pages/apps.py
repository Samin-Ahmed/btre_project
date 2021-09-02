from django.apps import AppConfig

# We added the "PagesConfig" to our "settings.py" "INSTALLED_APPS" list variable.


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
