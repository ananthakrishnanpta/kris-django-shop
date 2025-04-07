from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('user_type',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-control'
            if isinstance(field.widget, forms.Select):
                css_class = 'form-select'
            field.widget.attrs.update({'class': css_class})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
