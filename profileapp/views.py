from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    # 검증이후에 최종적으로하는 거...?!!?
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


