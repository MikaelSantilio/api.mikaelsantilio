from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128)
    from_email = forms.CharField(label='E-mail', max_length=128)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['from_email']
        message = self.cleaned_data['message']

        mail = EmailMessage(
            subject=f'[🔴LEAD do portfólio mikaelsantilio.github.io] {name} entrou em contato',
            body=message,
            from_email=from_email,
            to=['mikael.santilio@gmail.com'],
            reply_to=['mikael.santilio@gmail.com'],
            headers={'Message-ID': 'PORTFOLIO'},

        )

        mail.send()
