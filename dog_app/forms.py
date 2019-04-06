from django import forms


class DogForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DogForm, self).__init__(*args, **kwargs)
        if kwargs:
            # self.fields['name'].widget.attrs['value'] = 'name'
            # self.fields['breed'].widget.attrs['value'] = 'breed'
            self.fields['name'].widget.attrs['value'] = kwargs.clear()
            self.fields['breed'].widget.attrs['value'] = kwargs.clear()

    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'id': 'name',
    }))

    breed = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'id': 'breed',
    }))
