from django.core.validators import MinLengthValidator
from django.db import models


class Directory(models.Model):
    """
    Модель справочника
    """
    title = models.CharField(
        max_length=200,
        unique=True,
        validators=[MinLengthValidator(10)],
        help_text="10-200 символов. Должно быть уникально",
        verbose_name="Наименование",
    )
    alias = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        help_text="5-50 символов",
        verbose_name="Короткое наименование",
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        null=False,
        default="",
        help_text="0-1000 символов",
        verbose_name="Описание",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "справочник"
        verbose_name_plural = "справочники"
        ordering = ("title",)


class DirectoryVersion(models.Model):
    """
    Модель версии справочника
    """
    version = models.CharField(
        max_length=100,
        help_text="1-100 символов. Должна быть уникальна в пределах справочника",
        verbose_name="Версия справочника",
    )
    directory = models.ForeignKey(
        "Directory",
        on_delete=models.CASCADE,
        related_name="versions",
        related_query_name="version",
        verbose_name="Справочник",
    )
    actual_from_dt = models.DateField(
        verbose_name="Дата начала действия версии",
    )

    def __str__(self):
        return f"{self.directory.title}, версия: {self.version}"

    class Meta:
        verbose_name = "версия справочника"
        verbose_name_plural = "версии справочника"
        ordering = ("-actual_from_dt",)

        constraints = [
            # версия должна быть уникальна в пределах справочника
            models.UniqueConstraint(
                fields=("directory", "version"),
                name="%(app_label)s_%(class)s_unique_version",
            ),
            # дата должна быть уникальна для каждой версии
            models.UniqueConstraint(
                fields=("directory", "actual_from_dt"),
                name="%(app_label)s_%(class)s_unique_actual_from_dt",
            )
        ]


class DirectoryItem(models.Model):
    """
    Модель элемента справочника
    """
    code = models.CharField(
        max_length=100,
        help_text="1-100 символов. Должен быть уникален в пределах сравочника",
        verbose_name="Код",
    )
    value = models.TextField(
        max_length=1000,
        help_text="1-1000 символов",
        verbose_name="Значение элемента",
    )
    directory = models.ForeignKey(
        "Directory",
        on_delete=models.CASCADE,
        related_name="items",
        related_query_name="item",
        verbose_name="Справочник",
    )
    version = models.ForeignKey(
        "DirectoryVersion",
        on_delete=models.CASCADE,
        related_name="items",
        related_query_name="item",
        verbose_name="Версия",
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "элемент справочника"
        verbose_name_plural = "элементы справочника"
        ordering = ("code",)

        constraints = [
            # элемент справочника должен быть уникален в пределах справочника
            models.UniqueConstraint(
                fields=("directory", "code"),
                name="%(app_label)s_%(class)s_unique_code"
            )
        ]
