# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # Keep this import
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm # Import CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    """
    Custom UserAdmin for CustomUser model.
    Overrides default forms and fieldsets to include 'user_type' and handle CustomUser fields.
    """
    # Use your custom forms for adding and changing users
    form = CustomUserChangeForm # Use this form when editing an existing user
    add_form = CustomUserCreationForm # Use this form when adding a new user

    # The model this admin configuration is for
    model = CustomUser

    # The fields to display in the user list view of the admin
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active') # Corrected list display

    # Add 'user_type' to filters in the right sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_type')

    # Explicitly define the fieldsets for changing an existing user
    # This structure is similar to Django's default, but customized for CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}), # Base fields for authentication
        ('Personal info', {'fields': ('email', 'user_type')}), # Your custom user_type field
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Explicitly define the fieldsets for adding a new user
    # This structure focuses on the fields needed for creation via CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'user_type', 'password', 'password2'), # password and password2 are handled by CustomUserCreationForm
        }),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

# Register your CustomUser model with the admin site, using your custom admin class.
admin.site.register(CustomUser, CustomUserAdmin)
