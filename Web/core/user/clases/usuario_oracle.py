from core.personal.models.personal.models import VtUsuarioOracle
from core.user.models import User
from django.contrib.auth.hashers import make_password


########## Borrar usuario Oracle #########
def BorrarUserOracle():
    u = User.objects.filter(is_user_oracle='S')
    for reg in u:
        reg.delete()


def CrearUserOracle():
    # BorrarUserOracle()
    user_oracle = VtUsuarioOracle.objects.filter(usuario_oracle__isnull=False,).exclude(usuario_oracle__in=['JUANSOLANO'])
    usuario = ''
    data = {}
    for reg in user_oracle:
        try:
            usuario = reg.usuario_oracle
            passw = make_password(usuario)
            regC = User.objects.get(username=usuario,
                                    is_user_oracle='S',
                                    first_name=reg.nombre,
                                    last_name=reg.apellido,)
            if not regC:
                regC = User(username = usuario,
                            password = passw,
                            is_user_oracle = 'S',
                            first_name=reg.nombre,
                            last_name=reg.apellido,
                            email=reg.e_mail_institucional,
                            )
                regC.save()
            else:
                regC.cod_personal = reg.cod_personal
                regC.save()

            # if reg.codigo_cargo in [2, 3, 7, 21, 29, 34, 45, 47, 57, 62, 126, 136, 144]:
                ### is_group 7 ---> Ventas
                # regC.groups.add(7)
            # Grupo 5 Auditoria
            # regC.groups.add(5)
            regC.groups.remove(5)
        except Exception as e:
            print(e)
            data[usuario] = str(e)
    print('Creacion de usuarios Termianda')
    if len(data) == 0: return ('Lectura exitosa de registros')
    return ('Ha ocurrido un error: ' + str(data))