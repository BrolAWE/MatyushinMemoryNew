from django import forms

from core.models import Member, Answer, Update

TRUE_FALSE_CHOICES = (
    (False, 'Нет'),
    (True, 'Да'),
)


class MemberForm(forms.ModelForm):
    """Форма создания участника"""
    show_first = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Показать первую часть:",
                                   initial='', widget=forms.Select(), required=True)

    class Meta:
        model = Member
        fields = '__all__'
        exclude = ('experiment',)


class AnswerForm(forms.ModelForm):
    """Форма ответа"""
    answer = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Была ли такая таблица?",
                               initial='', widget=forms.Select(), required=True)

    class Meta:
        model = Answer
        fields = '__all__'
        exclude = ('member', 'table', 'was_shown', 'image', 'answer_time')


class UpdateForm(forms.ModelForm):
    """Форма обновления базы данных"""

    class Meta:
        model = Update
        fields = '__all__'
