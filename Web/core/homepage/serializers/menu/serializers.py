########## CONFIGURACION DE MENU ##############
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.homepage.models.menu.models import sidebarMenuDet

class subMenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model = sidebarMenuDet
        fields = ('id', 'parent_id', 'nombre', 'url', 'imagen')


class subMenuSerializer1(serializers.ModelSerializer):
    submenu = SerializerMethodField()

    def get_submenu(self, obj):
        items = sidebarMenuDet.objects.filter(parent_id=obj.id)
        serializer = subMenuSerializer2(instance=items, many=True)
        return serializer.data

    class Meta:
        model = sidebarMenuDet
        fields = ('id', 'parent_id', 'nombre', 'url', 'imagen', 'submenu')


class menuSerializer(serializers.ModelSerializer):
    submenu = SerializerMethodField()

    def get_submenu(self, obj):
        items = sidebarMenuDet.objects.filter(parent_id=obj.id)
        serializer = subMenuSerializer1(instance=items, many=True)
        return serializer.data

    class Meta:
        model = sidebarMenuDet
        fields = ('id', 'nombre', 'url', 'imagen','submenu')