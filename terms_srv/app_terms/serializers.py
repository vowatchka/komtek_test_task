from rest_framework import serializers

from .models import Directory, DirectoryVersion, DirectoryItem


class DirectoryVersionSerializer(serializers.ModelSerializer):
    """
    Сериалайзер версии справочника
    """

    class Meta:
        model = DirectoryVersion
        fields = ("version", "actual_from_dt")


class DirectorySerializer(serializers.ModelSerializer):
    """
    Сериалайзер справочника
    """
    versions = DirectoryVersionSerializer(many=True, read_only=True, help_text="Версии")
    items = serializers.HyperlinkedIdentityField(view_name="directory-items-list", lookup_url_kwarg="directory_pk",
                                                 read_only=True, help_text="Элементы справочника")

    class Meta:
        model = Directory
        # не используем ``__all__``, чтобы указать порядок полей
        fields = ("id", "title", "alias", "description", "versions", "items")


class DirectoryItemSerializer(serializers.ModelSerializer):
    """
    Сериалайзер элемента справочника
    """
    directory = serializers.HyperlinkedRelatedField(view_name="directory-detail", read_only=True,
                                                    help_text="Справочник")
    added_in = DirectoryVersionSerializer(source="version", help_text="Версия, в которой появился элемент")

    class Meta:
        model = DirectoryItem
        fields = ("id", "code", "value", "added_in", "directory")


class DirectoryItemsValidateSerializer(serializers.Serializer):
    """
    Сериалайзер запроса на валидацию элементов справочника
    """
    codes = serializers.ListField(
        child=serializers.CharField(max_length=100),
        allow_empty=False,
        help_text="Список валидируемых кодов элементов справочника",
    )
