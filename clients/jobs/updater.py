
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api
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

        # Iniciar el planificador en segundo plano
    scheduler.start()


    