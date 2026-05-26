from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "What needs to be done?"
            }),
            "deadline": forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }, format="%Y-%m-%dT%H:%M"),
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].input_formats = ["%Y-%m-%dT%H:%M"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Tag name"
            })
        }
