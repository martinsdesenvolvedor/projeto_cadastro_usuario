from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'email', 'whatsapp', 'username')
    list_filter = ('first_name', 'email', 'whatsapp', 'username')

    add_form_template: None
    add_form: CustomUserCreationForm
    form: CustomUserChangeForm
    model: CustomUser

    # campos a serem exibidos ao adicionar um usuário
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'first_name', 
                    'email',
                    'whatsapp',
                    'username',
                    'password1',
                    'password2'
                ),
            },
        ),
    )

    # campos a serem exibidos ao editar um usuário
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Complemento do Usuário',
            {
                'fields': (
                    'whatsapp',
                    
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
