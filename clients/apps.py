from django.apps import AppConfig

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    # def ready(self):
    #     from .jobs import updater
    #     updater.start()
    #     updater.notificar_piloto()
    #     updater.notificar_aeronave()
    #     updater.notificar_mecanico()