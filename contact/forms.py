from django import forms
__author__ = 'user'

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
       super(ContactForm, self).__init__(*args, **kwargs)
       for field in self.fields:
           self.fields[field].widget.attrs['class'] = 'form-control'

