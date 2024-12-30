import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from celery_config import celery_app
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@celery_app.task(bind=True, max_retries=3, default_retry_delay=5)
def send_email_task(self, smtp_server, smtp_port, email, password, recipient, subject, body):
    """
    Celery task to send an email with retry mechanism.
    """
    try:
        message = MIMEMultipart()
        message["From"] = email
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, recipient, message.as_string())

        logger.info(f"Email successfully sent to {recipient} with subject '{subject}'")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {recipient}: {e}")
        raise self.retry(exc=e)
