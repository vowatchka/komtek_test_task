from django import forms
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from .models import DirectoryVersion, DirectoryItem


class DirectoryVersionForm(forms.ModelForm):
    """
    Форма для занесения данных в версию справочника
    """

    class Meta:
        model = DirectoryVersion
        fields = "__all__"

    def clean(self):
        super().clean()

        # если справочник или дата не введены, то полагаемся на Django
        if "directory" not in self.cleaned_data or "actual_from_dt" not in self.cleaned_data:
            return

        errors = {}
        directory = self.cleaned_data["directory"]
        actual_from_dt = self.cleaned_data["actual_from_dt"]

        # берем последнюю версию справчоника
        last_version = self._meta.model.objects.only("version", "actual_from_dt").filter(directory=directory).first()
        if last_version is None:
            # если в справочнике нет версий, то новую версию можно добавить
            return

        if actual_from_dt > last_version.actual_from_dt:
            # если дата начала действия новой версии больше даты начала действия
            # последней версии, то новую версию можно добавить
            return

        errors["actual_from_dt"] = ValidationError(
            "Дата начала действия версии не может быть меньше либо равна"
            f" даты начала действия последней версии {last_version.version} ({last_version.actual_from_dt})"
        )
        raise ValidationError(errors)


class DirectoryItemForm(forms.ModelForm):
    """
    Форма для занесения данных в элемент справочника
    """

    class Meta:
        model = DirectoryItem
        exclude = ("directory",)

    def clean(self):
        super().clean()

        # если код или версия не введены, то полагаемся на Django
        if "code" not in self.cleaned_data or "version" not in self.cleaned_data:
            return

        errors = {}
        code = self.cleaned_data["code"]
        version = self.cleaned_data["version"]

        if self._meta.model.objects.filter(code=code, directory=version.directory).exists():
            errors[NON_FIELD_ERRORS] = ValidationError(
                "Элемент справочника с такими значениями полей Справочник и Код уже существует."
            )
            raise ValidationError(errors)

        return None
