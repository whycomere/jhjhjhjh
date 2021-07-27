from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):

        # 타겟유저 받아오는방법은 DB에접근해서 받아온다아!!! User.objects.all() ---->  모든것이아니라 특정한것만가져온다..!
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated
