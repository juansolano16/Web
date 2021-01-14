from datetime import datetime

from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from crum import get_current_request


class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return context


class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_permission(self):
        if isinstance(self.permission_required, str):
            perm = (self.permission_required,)
        else:
            perm = self.permission_required
        return perm

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_permission()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tienen permisos para ingresar a este modulo')
        return redirect(self.get_url_redirect())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return context


class GroupRequiredMixin(object):
    group_required = None
    url_redirect = None

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        user_groups = [g for g in request.user.groups.values_list('name', flat=True)]
        if len(set(user_groups).intersection(self.group_required)) <= 0 and not request.user.is_superuser:
            messages.error(request, 'No tienen permisos para ingresar a este modulo')
            return redirect(self.get_url_redirect())
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return context


class GroupRequiredMixin2(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        perms = []
        if isinstance(self.permission_required, str):
            perms.append(self.permission_required)
        else:
            perms = list(self.permission_required)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if 'group' in request.session:
            group = request.session['group']
            perms = self.get_perms()
            for p in perms:
                if not group.permissions.filter(codename=p).exists():
                    messages.error(request, 'No tiene permiso para ingresar a este módulo2')
                    return HttpResponseRedirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())
