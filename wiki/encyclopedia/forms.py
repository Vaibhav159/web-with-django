from django import forms


class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="Entry title",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-8 col-lg-8'
            }))

    content = forms.CharField(
        label="Enter the Content in Markdown",
        widget=forms.Textarea(
            attrs={'class': 'form-control col-md-8 col-lg-8',
                   'rows': 20
                   }))

    edit = forms.BooleanField(
        initial=False,
        widget=forms.HiddenInput(),
        required=False
    )
