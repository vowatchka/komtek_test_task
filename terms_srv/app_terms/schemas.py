from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import DirectoryItemsValidateSerializer


# часто используемые параметры
page_param = openapi.Parameter(
    "page",
    openapi.IN_QUERY,
    description="Номер страницы",
    type=openapi.TYPE_INTEGER,
)
directory_pk_param = openapi.Parameter(
    "directory_pk",
    openapi.IN_PATH,
    description="Уникальный идентификатор справочника",
    type=openapi.TYPE_INTEGER,
)
version_param = openapi.Parameter(
    "version",
    openapi.IN_QUERY,
    description="Фильтр элементов справочника по указанной версии",
    type=openapi.TYPE_STRING,
)

# описание схемы списка справочников
directories_list_schema = swagger_auto_schema(
    operation_description="",
    operation_summary="Получить список справочников",
    manual_parameters=[
        openapi.Parameter(
            "actual_before_dt",
            openapi.IN_QUERY,
            description="Фильтр справочников актуальных на указанную дату",
            type=openapi.TYPE_STRING,
        ),
        page_param,
    ],
)

# описание схемы одного справочника
directories_read_schema = swagger_auto_schema(
    operation_description="",
    operation_summary="Получить справочник",
    manual_parameters=[
        openapi.Parameter(
            "id",
            openapi.IN_PATH,
            description="Уникальный идентификатор справочника",
            type=openapi.TYPE_INTEGER,
        ),
    ],
)

# описание схемы элементов справочника
directories_items_list_schema = swagger_auto_schema(
    operation_description="",
    operation_summary="Получить элементы справочника",
    manual_parameters=[
        directory_pk_param,
        version_param,
        page_param,
    ],
)

# описание схемы одного элемента справочника
directories_items_read_schema = swagger_auto_schema(
    operation_description="",
    operation_summary="Получить элемент справочника",
    manual_parameters=[
        directory_pk_param,
        openapi.Parameter(
            "id",
            openapi.IN_PATH,
            description="Уникальный идентификатор элемента справочника",
            type=openapi.TYPE_INTEGER,
        ),
    ],
)

# описание схемы валидации элементов справочника
directories_items_validate = swagger_auto_schema(
    operation_description="",
    operation_summary="Валидация элементов справочника",
    manual_parameters=[
        directory_pk_param,
        version_param,
    ],
    request_body=DirectoryItemsValidateSerializer,
    responses={
        200: openapi.Response(
            "Отвалидированный набор элементов справочника,"
            " где каждому элементу справочника соответствует значение true,"
            " если элемент есть в справочнике, и false в противном случае",
            schema=openapi.Schema(
                type="object",
                addirionalProperties=[
                    openapi.Schema(type="bool"),
                ]
            ),
            examples={
                "application/json": {
                    "item1": True,
                    "item2": False,
                    "item3": True,
                }
            }
        ),
    },
)
