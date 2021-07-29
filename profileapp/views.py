from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# 로그인을 하는 데코레이터 적용하기..!!

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'


    # 검증이후에 최종적으로하는 거...?!!?
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    # 프로파일을 어떤이름을 불러올것인지!!
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm

    # success_url = reverse_lazy('accountapp:detail') 이라고 사용하지못하는이유..?

    template_name = 'profileapp/update.html'

    #내부메서드 오버라이딩
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


