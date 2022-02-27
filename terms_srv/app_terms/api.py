from django.utils.decorators import method_decorator
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Directory, DirectoryItem
from .serializers import DirectorySerializer, DirectoryItemSerializer, \
    DirectoryItemsValidateSerializer
from .filters import DirectoryFilter, DirectoryItemFilter
from .schemas import directories_list_schema, directories_read_schema, \
    directories_items_list_schema, directories_items_read_schema, \
    directories_items_validate


@method_decorator(name="list", decorator=directories_list_schema)
@method_decorator(name="retrieve", decorator=directories_read_schema)
class DirectoryApiView(ReadOnlyModelViewSet):
    """
    Представление справочников
    """
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DirectoryFilter


@method_decorator(name="list", decorator=directories_items_list_schema)
@method_decorator(name="retrieve", decorator=directories_items_read_schema)
@method_decorator(name="validate", decorator=directories_items_validate)
class DirectoryItemApiView(ReadOnlyModelViewSet):
    """
    Представление элементов справочников
    """
    serializer_class = DirectoryItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DirectoryItemFilter

    authentication_classes = []

    def get_queryset(self):
        return DirectoryItem.objects.filter(directory=self.kwargs.get("directory_pk", None))

    @action(detail=False, methods=["post"])
    def validate(self, request, *args, **kwargs):
        serializer = DirectoryItemsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        requested_codes = serializer.data["codes"]

        # фильтруем записи, сели есть фильтры в запросе
        qs = self.filter_queryset(self.get_queryset())

        codes = []
        # если в отфильтрованном наборе есть записи,
        # то можно проверить, есть ли среди них с такими кодами,
        # которые указаны в запросе
        if len(qs):
            codes = list(qs.filter(code__in=requested_codes).distinct().values_list("code", flat=True))

        # сформировать респонс, проставив каждому запрошенному коду
        # значение True, если элемент с таким кодом отфильтровался,
        # и False в противном случае
        return Response(
            {code: (code in codes) for code in requested_codes}
        )
