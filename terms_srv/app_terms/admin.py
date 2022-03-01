from django.contrib import admin
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from django.utils.html import format_html

from .models import Directory, DirectoryVersion, DirectoryItem
from .forms import DirectoryVersionForm, DirectoryItemForm


# Кол-во записей в списке записей
LIST_PER_PAGE = 10


@admin.display(description="Справочник", ordering="directory__title")
def directory_view(obj):
    """
    Выводит ссылку на справочник
    """
    return format_html(
        '<a href="{}?pk={}">{}</a>',
        reverse("admin:app_terms_directory_changelist"),
        obj.directory.pk,
        obj.directory.title
    )


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    """
    Админка для справочника
    """

    list_display = ("id", "title", "alias", "description_view", "version_count_view", "item_count_view")
    list_display_links = ("id", "title")

    search_fields = ("title",)

    list_per_page = LIST_PER_PAGE

    @admin.display(description="Описание")
    def description_view(self, obj):
        """
        Выводит описание справочника, урезанное до 15 слов
        """
        return truncatewords(obj.description, 15)

    @admin.display(description="Количество элементов")
    def item_count_view(self, obj):
        """
        Выводит количество элементов справочника, обернутое в ссылку на
        все элементы этого справочника
        """
        return format_html(
            '<a href="{}?directory={}">{}</a>',
            reverse("admin:app_terms_directoryitem_changelist"),
            obj.pk,
            obj.items.count()
        )

    @admin.display(description="Количество версий")
    def version_count_view(self, obj):
        """
        Выводит количество версий справочника, обернутое в ссылку на
        все версии этого справочника
        """
        return format_html(
            '<a href="{}?directory={}">{}</a>',
            reverse("admin:app_terms_directoryversion_changelist"),
            obj.pk,
            obj.versions.count()
        )


@admin.register(DirectoryVersion)
class DirectoryVersionAdmin(admin.ModelAdmin):
    """"
    Админка для версии справочника
    """

    list_display = ("id", "version", "actual_from_dt", directory_view)
    list_display_links = ("id", "version")
    ordering = ("directory__title", "-actual_from_dt")

    search_fields = ("directory__title",)
    list_filter = ("actual_from_dt",)

    form = DirectoryVersionForm

    list_per_page = LIST_PER_PAGE


@admin.register(DirectoryItem)
class DirectoryItemAdmin(admin.ModelAdmin):
    """
    Админка для элемента справочника
    """

    list_display = ("id", "code", "value_view", directory_view, "version_view")
    list_display_links = ("id", "code")
    ordering = ("directory__title", "code")

    search_fields = ("code", "value")

    form = DirectoryItemForm

    list_per_page = LIST_PER_PAGE

    @admin.display(description="Значение элемента")
    def value_view(self, obj):
        """
        Выводит значение справочника, урезанное да 15 слов
        """
        return truncatewords(obj.value, 15)

    @admin.display(description="Версия")
    def version_view(self, obj):
        """
        Выводит ссылку на версию, в которой появился данный элемент справочника
        """
        return format_html(
            '<a href="{}?pk={}">{}</a>',
            reverse("admin:app_terms_directoryversion_changelist"),
            obj.version.pk,
            obj.version.version
        )

    def save_model(self, request, obj, form, change):
        obj.directory = form.cleaned_data["version"].directory
        super().save_model(request, obj, form, change)
