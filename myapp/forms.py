from django import forms
from .models import EventRequest, CeremonyActivity
from django.core.exceptions import ValidationError


class EventRequestForm(forms.ModelForm):
    """
    Form for creating or updating event requests.
    """

    class Meta:
        model = EventRequest
        fields = ['titulo', 'descripcion', 'lugar', 'fecha_inicio', 'fecha_fin',
                  'presupuesto', 'alimentacion', 'transporte', 'profesor']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        }

    def clean(self):
        """
        Custom form validation.
        """
        cleaned_data = super().clean()
        lugar = cleaned_data.get('lugar')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        presupuesto = cleaned_data.get('presupuesto')

        if not lugar or not fecha_inicio or not fecha_fin or not presupuesto:
            raise forms.ValidationError(
                'Ninguno de los campos puede estar vacío.')

        if fecha_inicio and fecha_fin:
            if fecha_inicio > fecha_fin:
                raise forms.ValidationError(
                    'La fecha de inicio no puede ser posterior a la fecha de fin.')

        if presupuesto and presupuesto < 0:
            raise forms.ValidationError(
                'El presupuesto no puede ser negativo.')


class EstadoSolicitudForm(forms.Form):
    """
    Form for updating the status of event requests.
    """
    evento_id = forms.IntegerField(widget=forms.HiddenInput)
    estado_solicitud = forms.CharField(label='Estado de la Solicitud', widget=forms.Select(
        choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')]))


class CeremonyActivityForm(forms.ModelForm):
    """
    Form for creating or updating ceremony activities.
    """
    class Meta:
        model = CeremonyActivity
        fields = ['title']
