import django_filters
from django.db.models import QuerySet

from .models import Directory, DirectoryVersion, DirectoryItem


class DirectoryFilter(django_filters.FilterSet):
    """
    Фильтр справочников
    """

    # Применение этого фильтра вернет справочники,
    # дата начала действия версии которых
    # меньше либо равна указанной.
    actual_before_dt = django_filters.DateFilter(
        field_name="version__actual_from_dt",
        distinct=True,
        lookup_expr="lte",
    )

    class Meta:
        model = Directory
        fields = ("actual_before_dt",)


class DirectoryItemFilter(django_filters.FilterSet):
    """
    Фильтр элементов справочника
    """

    # Применение этого фильтра вернет элементы справочника
    # указанной версии.
    #
    # При отсутствии фильтра возвращаются все элементы справочника,
    # т.е. элементы справочника текущей версии (последней).
    version = django_filters.CharFilter(method="filter_by_version")

    class Meta:
        model = DirectoryItem
        fields = ("version",)

    def filter_by_version(self, queryset, name, value):
        """
        Метод для фильтрации элементов справочника по указанной версии
        """

        filters = {
            name: value,
            "directory": self.request.parser_context["kwargs"]["directory_pk"]
        }

        # находим указанную версию
        version = DirectoryVersion.objects.only("actual_from_dt").filter(**filters).first()
        if version is not None:
            # возвращаем все элементы справчоника указанной версии,
            # т.е. такие, которые были добавлены в указанную версию
            # и во все версии до нее
            return queryset.filter(version__actual_from_dt__lte=version.actual_from_dt)
        # если не нашли версию, то возвращаем пустой QuerySet
        return queryset.none()
