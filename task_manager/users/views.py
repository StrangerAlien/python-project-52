from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class CreateUserView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    template_name = 'create.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User successfully registered')


class ReadUserView(ListView):
    model = get_user_model()
    template_name = 'read.html'
    context_object_name = 'users'


class UpdateUserView(UpdateView):
    model = get_user_model()
    template_name = 'update.html'
    form_class = UserForm
    success_message = _('User successfully updated')
    success_url = reverse_lazy('users')


class DeleteUserView(DeleteView):
    model = get_user_model()
    template_name = 'delete.html'
    success_url = reverse_lazy('users')
    success_message = _("User successfully deleted")
