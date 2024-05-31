from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.xls', '.xlsx')):
            raise forms.ValidationError('Invalid file type. Only Excel files are allowed.')
        return file