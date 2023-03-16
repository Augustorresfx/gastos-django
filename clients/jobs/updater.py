
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api, expiracion_pilotos, expiracion_aeronaves, expiracion_mecanicos
from datetime import datetime, time
def start():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(schedule_api, 'cron', day_of_week='mon-fri', hour=19, minute=00)
    #scheduler.add_job(schedule_api, 'interval', seconds=5)
        # Iniciar el planificador en segundo plano
    scheduler.start()


def notificar_piloto():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_pilotos, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()

def notificar_aeronave():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()
    
def notificar_mecanico():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_mecanicos, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()
    
    

    