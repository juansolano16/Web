from django.urls import path

from core.notificaciones.views.correo.views import sendMail, send_user_mail, sendMailContact
from core.notificaciones.views.sms.views import sms

app_name = 'notificaciones'

urlpatterns = [
    path('sendMail/', sendMail),
    path('sendMail2/', send_user_mail),
    path('sendEmailContact/', sendMailContact, name='sendEmailContact'),
    path('sms/', sms),
]