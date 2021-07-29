from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


# 로그인여부를하고 리다이렉트까지 해줌...!!! 원래짰었던 /accounts/login/ 장고 기본주소이기때문에
@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("hello_world_input")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    # return render(request, 'accountapp/hello_world.html',
    #               context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
    # context={'text': 'get method!'})


# def hello_world(request):
#     return render(request, 'accountapp/hello_world.html')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = "target_user"
    template_name = 'accountapp/detail.html'


#     연결 라우팅을 해줘야한다!!

has_ownership = [login_required, account_ownership_required]


@method_decorator(has_ownership, 'post')
@method_decorator(has_ownership, 'get')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = "target_user"

    # success_url = reverse_lazy("accountapp:hello_world")

    template_name = 'accountapp/update.html'


    def get_success_url(self):
        # user을 안찾아가도됨!!
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

    # # 함수가아니라 클래스안에 메소드임으로 데코레이터자체를 사용하지못한다..!!클래스 데코 , 변환코드
    #
    # def get(self, request, *args, **kwargs):
    #
    #     # get_object 는 타겟 오브젝트랑 똑같음...!!
    #
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #
    #         # 부모메소드 겟해줌
    #
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #
    #         # 부모메소드 겟해줌
    #
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         # 부모메소드 겟해줌
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    #             # HttpResponseRedirect(reverse('accountapp:login'))
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         # 부모메소드 겟해줌
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
