from django import forms
from .models import Materia

DIAS_DA_SEMANA = [
    (2, 'Segunda-feira'),
    (3, 'Terça-feira'),
    (4, 'Quarta-feira'),
    (5, 'Quinta-feira'),
    (6, 'Sexta-feira'),
    (7, 'Sábado'),
]

class MateriaForm(forms.ModelForm):
    dias_da_semana = forms.MultipleChoiceField(choices=DIAS_DA_SEMANA, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Materia
        fields = ['nome', 'semestre', 'dias_da_semana']

    def __init__(self, *args, **kwargs):
        # Pegando a turma para obter o período e definir os horários
        self.turma = kwargs.pop('turma', None)
        super().__init__(*args, **kwargs)

        # Horários pré-fixados de acordo com o período da turma
        self.horarios_prefixed = {
            1: ['07:40 - 08:30', '08:30 - 09:20', '09:30 - 10:20', '10:20 - 11:10', '11:20 - 12:10', '12:10 - 13:00'],  # Matutino
            2: ['13:50 - 14:40', '14:50 - 15:40', '15:40 - 16:30', '16:30 - 17:20', '17:20 - 18:10'],  # Vespertino
            3: ['19:00 - 19:50', '19:50 - 20:40', '20:50 - 21:40', '21:40 - 22:30']  # Noturno
        }

        # Se a instância da matéria já existir, preencha os dados de dias e horários
        if self.instance and self.instance.horarios_por_dia:
            # Preenche os checkboxes de dias da semana
            dias_selecionados = list(self.instance.horarios_por_dia.keys())
            self.fields['dias_da_semana'].initial = dias_selecionados
            
            # Dicionário temporário para armazenar horários
            horarios_temp = {}
            for dia in dias_selecionados:
                horarios = self.instance.horarios_por_dia[dia]
                # Adiciona os horários ao dicionário temporário
                if isinstance(horarios, list):
                    horarios_temp[dia] = horarios
                else:
                    horarios_temp[dia] = [horarios]
            
            # Preenche os horários na instância do formulário
            for dia, horarios in horarios_temp.items():
                # Armazena os horários na forma de uma lista
                self.initial[f'horarios_{dia}'] = horarios

    def clean(self):
        cleaned_data = super().clean()
        dias = cleaned_data.get('dias_da_semana')

        horarios_por_dia = {}

        # Iterando sobre os dias da semana selecionados
        for dia in dias:
            # Coleta todos os horários marcados para o dia específico
            horarios = self.data.getlist(f'horarios_{dia}')
            if horarios:
                horarios_por_dia[dia] = horarios

        # Verificação se pelo menos um horário foi selecionado para algum dia
        if not horarios_por_dia:
            raise forms.ValidationError("Você deve selecionar pelo menos um horário para os dias escolhidos.")

        # Armazenar os horários organizados por dia no cleaned_data
        self.cleaned_data['horarios_por_dia'] = horarios_por_dia

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Organizando os horários por dia no campo JSON
        horarios_por_dia = self.cleaned_data['horarios_por_dia']
        instance.horarios_por_dia = horarios_por_dia

        if commit:
            instance.save()
        return instance
