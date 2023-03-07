from django import forms
from system.models.question import Question
from system.models.person import Person
from system.models.company import Company
from system.models.event import Event


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'question']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 15}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['approved']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['company_name'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['corporate_name'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['fantasy_name'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['cnpj'].widget.attrs.update({
    #         'class': 'form-control',
    #         'type': 'text',
    #         'placeholder': 'Apenas números.',
    #     })
    #     self.fields['position'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['cep'].widget.attrs.update({
    #         'class': 'form-control',
    #         'type': 'text',
    #         'data-plugin-masked-input': '',
    #         'data-input-mask': '99999-999',
    #     })
    #     self.fields['public_place'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['complement'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['neighborhood'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['city'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['state'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['number'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['phone'].widget.attrs.update({
    #         'data-plugin-masked-input': '',
    #         'data-input-mask': '(99) 99999-9999',
    #         'class': 'form-control',
    #         'type': 'text',
    #         'placeholder': '(00) 00000-0000',
    #     })
    #     self.fields['segmentation'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['approved', 'company']
        # opt_in = forms.BooleanField(widget=forms.RadioSelect(choices=OPT_IN_CHOICES))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text', 'required': True})
    #     self.fields['name_cracha'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text', 'required': True})
    #     self.fields['category'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text', 'required': True})
    #     self.fields['cell_phone'].widget.attrs.update({
    #         'data-plugin-masked-input': '',
    #         'data-input-mask': '(99) 99999-9999',
    #         'class': 'form-control',
    #         'type': 'text',
    #         'placeholder': '(00) 00000-0000',
    #         'required': True
    #     })
    #     self.fields['cpf'].widget.attrs.update({
    #         'class': 'form-control',
    #         'type': 'text',
    #         'placeholder': 'Apenas números.',
    #     })
    #     self.fields['email'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text', 'required': True})
    #     self.fields['role'].widget.attrs.update(
    #         {'class': 'form-control', 'type': 'text'})
    #     self.fields['phone'].widget.attrs.update({
    #         'data-plugin-masked-input': '',
    #         'data-input-mask': '(99) 99999-9999',
    #         'class': 'form-control',
    #         'type': 'text',
    #         'placeholder': '(00) 00000-0000',
    #     })


class AnsweredForm(forms.Form):
    def __init__(self, survey, *args, **kwargs):
        super(AnsweredForm, self).__init__(*args, **kwargs)
        self.fields['options'] = forms.ChoiceField(
            choices=[(option.id, option.desc)
                     for option in Alternative.objects.filter(survey=survey)],
            widget=forms.RadioSelect(),
        )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'type': 'type', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'type': 'type', 'class': 'form-control'})
        self.fields['cep'].widget.attrs.update({
            'class': 'form-control',
            'type': 'text',
            'data-plugin-masked-input': '',
            'data-input-mask': '99999-999',
        })
        self.fields['public_place'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})
        self.fields['complement'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})
        self.fields['neighborhood'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})
        self.fields['city'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})
        self.fields['state'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})
        self.fields['number'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})
        self.fields['first_date'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-datepicker': ''})
        self.fields['last_date'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-datepicker': ''})
        self.fields['first_hour'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text' })
        self.fields['last_hour'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-masked-input': '',
             'data-input-mask': '99:99', 'placeholder': '__:__' })
        self.fields['qtd_registration'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text'})

            
class CpfForm(forms.Form):
    cpf = forms.CharField(max_length=14)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-masked-input': '', 'data-input-mask': '999.999.999-99', })


class CnpjForm(forms.Form):
    cnpj = forms.CharField(max_length=18)
    term_check = forms.BooleanField(label='term_check', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cnpj'].widget.attrs.update(
            {'class': 'form-control', 'type': 'text', 'data-plugin-masked-input': '', 'data-input-mask': '00.000.000/0000-00', })

