from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from core.notificaciones.clases.sms import SendSms


@method_decorator(csrf_exempt)
def sms(request):
	if request.POST:
		try:
			num = request.POST['num']
			param = request.POST['param'].split('|')
			SendSms(num,param)
			return HttpResponse('ok post')
		except Exception as e:
			return HttpResponse('Ha ocurrido un error' + str(e))

	return HttpResponse('ok get')
