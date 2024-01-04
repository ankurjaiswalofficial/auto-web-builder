from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'api_key',)  # Add fields that users need to fill in to obtain API access

    # You can customize form field behavior/validation if needed
