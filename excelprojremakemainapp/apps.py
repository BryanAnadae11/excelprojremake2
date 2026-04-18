from django.apps import AppConfig


class ExcelprojremakemainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'excelprojremakemainapp'

    def ready(self):
    	import excelprojremakemainapp.signals
