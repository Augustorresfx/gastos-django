from django.conf import settings
import os
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from datetime import timedelta, datetime
from ..models import Operacion
from openpyxl import load_workbook
from pathlib import Path
from datetime import date
from django.utils import timezone

load_dotenv()
def schedule_api():
    print("sending_email")
    BASE_DIR = Path(__file__).resolve().parent.parent
    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(BASE_DIR, 'static/Reporte_diario.xlsx')   #full path to text.
    
    path = file_path
    wb = load_workbook(path)
    wb.iso_dates = True
    sheet = wb.active
    max_col = sheet.max_column
    hoy = timezone.now().date()  # Obtiene la fecha actual
    objetos_hoy = Operacion.objects.filter(created__date=hoy)
    
    objetos_todos = Operacion.objects.all()
    

    for product in objetos_hoy:
        timeformat = "%H:%M:%S"
        delta = datetime.strptime(str(product.landing_time), timeformat) - datetime.strptime(str(product.takeoff_time), timeformat)
        
        data = [product.takeoff_place, product.created.strftime("%d %m %y"), '', product.pilot.name, product.mechanic.name, product.operator.name, product.aeronave.title, timedelta(seconds=delta.seconds), '', product.reason_of_flight.title, '', '', '', product.start_up_cycles, '', '', '', '', '', '', '', '', '', product.engine_ignition_1, product.engine_cut_1, product.engine_ignition_2, product.engine_cut_2]
    
        sheet.append(data)

    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    msg = MIMEMultipart()
    msg['From'] = 'no.reply.wings@gmail.com'
    msg['To'] = ', '.join(['augustorresfx@gmail.com',])
    msg['Subject'] = 'Su reporte del día'

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((excel_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='Reporte_Diario' + \
    str(datetime.now())+'.xlsx')
    msg.attach(part)

    html = """\
        <html>
        <head></head>
        <body>
            <h1>Estimado/a,</h1>
            <h2>Adjunto encontrará el archivo de Excel con los datos solicitados:</h2>
        </body>
        </html>
        """
    msg.attach(MIMEText(html, 'html'))

    # Conectar y enviar el correo electrónico
    smtp_server = 'smtp.gmail.com'  # Cambia esto a tu servidor SMTP
    smtp_port = 587  # Cambia esto al puerto de tu servidor SMTP
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')  # Cambia esto a tu contraseña SMTP
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_user, smtp_password)
    smtp_connection.sendmail(smtp_user, msg['To'], msg.as_string())
    smtp_connection.quit()
    print("Sended")