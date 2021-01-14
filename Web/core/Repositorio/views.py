from django.http.response import JsonResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import config.settings as setting

@method_decorator(csrf_exempt)
def RevistaUnno(request):
    # if request.POST;
    data = {}
    try:
        path = setting.BASE_DIR + '/core/Repositorio/docs/RevistaContigo_Sep2020.pdf'
        response = FileResponse(open(path, 'rb'), as_attachment=True, filename='RevistaContigo_Sep2020.pdf')
        return response
    except Exception as e:
        data['error'] = str(e)
    return JsonResponse(data)
