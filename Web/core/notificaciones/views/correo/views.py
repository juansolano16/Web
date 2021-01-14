import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from config import settings


@method_decorator(csrf_exempt)
def sendMail(request):
	if request.POST:
		subject = request.POST['asunto']
		message = request.POST['msj']
		email_from = settings.EMAIL_HOST_USER
		recipient_list = request.POST['to'].split(',')
		send_mail(subject, message, email_from, recipient_list)
		return HttpResponse('ok mail')
	return  HttpResponse('ok get mail')



@method_decorator(csrf_exempt)
def sendMailContact(request):
	if request.POST:
		# try:
			subject = request.POST['asunto']
			message = request.POST['msj']
			nombre = request.POST['name']
			correo = request.POST['email']
			to = ['juansolano@mastermoto.com.ec']

			template = get_template('correo/correo_msj.html')
			content = template.render({
				'nombre': nombre,
				'msj': message,
				'asunto': subject,
				'correo': correo
			})

			message = EmailMultiAlternatives('Nuevo mensaje',
											 'This is an important message.',
											 settings.EMAIL_HOST_USER,  # Remitente
											 to)  # Destinatario
			message.attach_alternative(content, 'text/html')

			for f in ['Img3_2x.jpg','user.png',]:
				message.attach_file(settings.BASE_DIR + '/core/notificaciones/static/img/' + f)
			message.send()
			return HttpResponse('Mensaje enviado, gracias!')
		# except Exception as e:
		# 	return HttpResponse('Error, al enviar msj: ' + str(e))
	return  HttpResponse('ok get mail')



def send_user_mail(request):
    subject = 'Titulo del correo'
    template = get_template('correo/correo.html')
    content = template.render({
        'user': 'juan',
    })
    text_content = 'This is an important message.'
    message = EmailMultiAlternatives(subject,
                                    text_content,
                                    settings.EMAIL_HOST_USER, #Remitente
                                    ['juansolano@mastermoto.com.ec']) #Destinatario
    message.attach_alternative(content, 'text/html')
    #message.attach_file('static/img/logo.png')
    message.send()

    return HttpResponse('ok')