from django.forms import Form, ModelForm
from django import forms
from .models import Test_Attempt, Test
from django.core.files import File
import json
import os
from . import file_methods
from django.core.validators import MaxValueValidator, MinValueValidator

class QuizShowForm(Form):

    def __init__(self, questions, *args, **kwargs):
        super(QuizShowForm, self).__init__(*args, **kwargs)
        self.questions = questions
        counter = [0, 0, 0]
        self.fields[f'quiz_show'] = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
        for question in self.questions:
            match question['type']:
                case 'TF':
                    counter[0] += 1
                    self.fields[f'TF_{counter[0]}'] = forms.ChoiceField(label=f'{question["text"]} ({question["mark"]} баллов)', required=True, 
                                        choices=(('True', 'Да'), ('False', 'Нет')), widget=forms.RadioSelect)
                case 'O':
                    counter[1] += 1
                    self.fields[f'O_{counter[1]}'] = forms.CharField(label=f'{question["text"]} ({question["mark"]} баллов)', widget=forms.Textarea) 
                case 'AO':
                    counter[2] += 1
                    choices = [(i, question['choices'][i-1]) for i in range(1, len(question['choices']) + 1)]
                    self.fields[f'AO_{counter[2]}'] = forms.ChoiceField(label=f'{question["text"]} ({question["mark"]} баллов)', required=True,
                                           choices=choices, widget=forms.RadioSelect)
    
    def save(self, solution, user, test, *args, **kwargs):
        interm_file_path = os.path.join(file_methods.PATH, 'intermediate_content', 
                              f'{file_methods.get_transliteration(test.name)}.json')
        f = open(interm_file_path, 'a+', encoding='utf-8')
        res_str = json.dumps(solution, indent = 2, ensure_ascii=False)
        f.write(res_str)
        test_attempt = Test_Attempt(test=test, student=user.student_profile, file=File(f))
        test_attempt.save()
        f.close()
        os.remove(interm_file_path)

class QuizUpdateForm(ModelForm):
    
    class Meta:
        model = Test
        fields = ['name', 'duration']
        widgets = {'duration': forms.widgets.TimeInput(attrs={'type': 'time'})}

class QuizPublishForm(Form):
    publish_st = forms.CharField(widget=forms.HiddenInput)

class QuizAttemptCheckForm(Form):
    def __init__(self, attempt, *args, **kwargs):
        super(QuizAttemptCheckForm, self).__init__(*args, **kwargs)
        counter = 0
        for ans in attempt:
            counter += 1
            self.fields[f'Answer{counter}'] = forms.IntegerField(label="", initial=attempt[ans][1])
            self.fields[f'Answer{counter}'].widget.attrs['class'] = 'ans-input'
            self.fields[f'Answer{counter}'].widget.attrs['max'] = attempt[ans][2]
            self.fields[f'Answer{counter}'].widget.attrs['min'] = 0

class QuizAttemptDeniedForm(Form):
    denied_st = forms.CharField(widget=forms.HiddenInput)
    
