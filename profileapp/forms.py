from django.forms import ModelForm

from profileapp.models import Profile

# 유저는 서버에서 집적해쥼

class ProfileCreationForm(ModelForm):
    # 이지나 외반적인 정보같은건 메타로...!!?!! 외부적인 정보
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

