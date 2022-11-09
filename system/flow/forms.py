from django import forms


class CpfForm(forms.Form):
    cpf = forms.CharField(max_length=14)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-masked-input': '', 'data-input-mask': '999.999.999-99', })


class CnpjForm(forms.Form):
    cnpj = forms.CharField(max_length=18)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cnpj'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-masked-input': '', 'data-input-mask': '00.000.000/0000-00', })


