from django import forms
from .models import Materia
from salas.models import Sala  # Importando o model Sala
from professors.models import Professor  # Importando o model Professor
from django.core.exceptions import ValidationError

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
    
    # Campo de seleção para o professor
    professor = forms.ModelChoiceField(queryset=Professor.objects.all(), required=False, label="Professor", empty_label="Selecione um professor")
    
    # Campo de seleção para a sala
    sala = forms.ModelChoiceField(queryset=Sala.objects.all(), required=False, label="Sala", empty_label="Selecione uma sala")

    class Meta:
        model = Materia
        fields = ['nome', 'dias_da_semana', 'professor', 'sala']  # Adicionado 'sala' aos campos do formulário

    def __init__(self, *args, **kwargs):
        self.turma = kwargs.pop('turma', None)
        super().__init__(*args, **kwargs)

        # Tornando o campo 'nome' não editável
        self.fields['nome'].disabled = True

        # Horários pré-fixados de acordo com o período da turma
        self.horarios_prefixed = {
            1: ['07:40 - 08:30', '08:30 - 09:20', '09:30 - 10:20', '10:20 - 11:10', '11:20 - 12:10', '12:10 - 13:00'],  # Matutino
            2: ['13:50 - 14:40', '14:50 - 15:40', '15:40 - 16:30', '16:30 - 17:20', '17:20 - 18:10'],  # Vespertino
            3: ['19:00 - 19:50', '19:50 - 20:40', '20:50 - 21:40', '21:40 - 22:30']  # Noturno
        }

        if self.instance and self.instance.horarios_por_dia:
            dias_selecionados = list(self.instance.horarios_por_dia.keys())
            self.fields['dias_da_semana'].initial = dias_selecionados

            horarios_temp = {}
            for dia in dias_selecionados:
                horarios = self.instance.horarios_por_dia[dia]
                if isinstance(horarios, list):
                    horarios_temp[dia] = horarios
                else:
                    horarios_temp[dia] = [horarios]

            for dia, horarios in horarios_temp.items():
                self.initial[f'horarios_{dia}'] = horarios

        # Pré-selecionar a sala que contém a matéria atual
        if self.instance.pk:
            salas = Sala.objects.filter(materias=self.instance)
            if salas.exists():
                self.fields['sala'].initial = salas.first()

    def clean(self):
        cleaned_data = super().clean()
        dias = cleaned_data.get('dias_da_semana')

        horarios_por_dia = {}
        for dia in dias:
            horarios = self.data.getlist(f'horarios_{dia}')
            if horarios:
                horarios_por_dia[dia] = horarios

        if not horarios_por_dia:
            raise forms.ValidationError("Você deve selecionar pelo menos um horário para os dias escolhidos.")

        self.cleaned_data['horarios_por_dia'] = horarios_por_dia
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        horarios_por_dia = self.cleaned_data['horarios_por_dia']
        
        # Verificar se um professor foi selecionado
        if instance.professor:
            try:
                # Subtrair as horas atuais do professor
                if instance.pk:  # Verifica se a instância já existe
                    horarios_atuais = instance.horarios_por_dia
                    total_horas_atuais = sum(len(horarios) for horarios in horarios_atuais.values())
                    print(total_horas_atuais)
                    instance.professor.remover_horarios(total_horas_atuais)

                # Adicionar as novas horas ao professor
                total_horas_novas = sum(len(horarios) for horarios in horarios_por_dia.values())
                instance.professor.adicionar_horarios(total_horas_novas)
            except ValidationError as e:
                self.add_error('professor', e.message)
                raise

        instance.horarios_por_dia = horarios_por_dia

        if commit:
            instance.save()

            # Associar a matéria à sala selecionada
            sala = self.cleaned_data.get('sala')
            if sala:
                sala.materias.add(instance)

        return instance