
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api, expiracion_pilotos, expiracion_aeronaves, expiracion_aeronaves_anexo_2, expiracion_aeronaves_notaciones_requerimiento, expiracion_aeronaves_inspeccion_anual, expiracion_mecanicos
from .jobs import expiracion_aeronaves_25, expiracion_aeronaves_50, expiracion_aeronaves_100
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

# AERONAVES VENCIMIENTOS FECHAS

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
    
def notificar_aeronave_anexo_2():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves_anexo_2, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()

def notificar_aeronave_notaciones_requerimiento():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves_notaciones_requerimiento, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()

def notificar_aeronave_inspeccion_anual():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves_inspeccion_anual, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()
    
# AERONAVES VENCIMIENTOS HORAS

def notificar_aeronave_25():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves_25, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()

def notificar_aeronave_50():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves_50, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()

def notificar_aeronave_100():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(expiracion_aeronaves_100, 'interval', days=1)

        # Iniciar el planificador en segundo plano
    scheduler.start()
    
# MECANICOS VENCIMIENTOS FECHAS

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
    
    

    