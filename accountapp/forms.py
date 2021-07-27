from django.contrib.auth.forms import UserCreationForm

class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 유저네임 필드를 비활성화
        self.fields['username'].disabled = True

