import ast

from core.homepage.models.menu.models import sidebarMenuDet, sidebarMenu
from core.homepage.serializers.menu.serializers import menuSerializer
from rest_framework.renderers import JSONRenderer




def get_menu(group):
    try:
        menu = sidebarMenu.objects.get(id_group=group)
        queryset = sidebarMenuDet.objects.filter(id_menuc_id=menu.id, parent_id__isnull=True)
        serializer = menuSerializer(queryset, many=True)
        js = JSONRenderer().render(serializer.data).decode('utf-8')
        res = ast.literal_eval(js)
        return res
    except:
        return None