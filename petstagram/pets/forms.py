from django import forms

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.Textarea(attrs={'placeholder': 'Link to image'}),
        }
        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }


class PetEditForm(PetForm):
    pass


class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
