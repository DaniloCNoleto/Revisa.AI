from django import forms

class UploadForm(forms.Form):
    documento = forms.FileField(label="Documento (.docx)", required=True)
