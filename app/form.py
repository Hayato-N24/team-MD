from django import forms

class InputForm(forms.Form):
    text = forms.CharField( label="",widget=forms.Textarea( attrs={'cols': '40', 'rows': '10'} ) )
