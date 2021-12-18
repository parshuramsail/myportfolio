from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'class': 'form-control', 'id': 'subject'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'email'}),
    )

    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Enter your message', 'class': 'form-control'}))
