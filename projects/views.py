from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings

from .forms import ContactForm
from .models import Project


class ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = Project  # data from database
    template_name = 'index.html'
    context_object_name = 'projects'  # name of the var in html template
    queryset = Project.objects.all()  # list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/'  # After submiting the form keep staying on the same url
    success_message = 'Your mail has been sent successfully!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            cd['email'],
            cd['message'],
            cd['name'],
            ['paresh581345@gmail.com'],
            fail_silently=False
        )
        return super(ProjectListAndFormView, self).form_valid(form)
