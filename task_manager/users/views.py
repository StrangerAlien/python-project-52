from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class CreateUserView(SuccessMessageMixin, CreateView):
    # template_name = 'create.html'
    pass


class ReadUserView(ListView):
    pass


class UpdateUserView(UpdateView):
    pass


class DeleteUserView(DeleteView):
    pass
# Create your views here.
