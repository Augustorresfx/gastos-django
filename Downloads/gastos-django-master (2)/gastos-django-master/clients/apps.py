from django.apps import AppConfig

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    def ready(self):
        from .jobs import updater
        updater.start()
        updater.notificar_piloto()
        updater.notificar_aeronave()
        updater.notificar_mecanico()
        updater.notificar_aeronave()
        updater.notificar_aeronave_anexo_2()
        updater.notificar_aeronave_notaciones_requerimiento()
        updater.notificar_aeronave_inspeccion_anual()
        updater.notificar_aeronave_25()
        updater.notificar_aeronave_50()
        updater.notificar_aeronave_100()