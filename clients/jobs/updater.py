import time
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from datetime import timedelta, datetime
import openpyxl
from openpyxl import load_workbook
from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from ..views import send_mail_with_excel
from .jobs import schedule_api
load_dotenv()

def start():
        # Crear un planificador en segundo plano
    job_defaults = {
    'coalesce': False,
    'max_instances': 1
    }
    scheduler = BackgroundScheduler(job_defaults=job_defaults)

        # Programar la tarea para que se ejecute todos los días a las 10:00 AM
    scheduler.add_job(schedule_api, 'interval', minutes=10)

        # Iniciar el planificador en segundo plano
    scheduler.start()


    