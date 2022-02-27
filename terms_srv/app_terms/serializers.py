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
    versions = DirectoryVersionSerializer(many=True, read_only=True)

    class Meta:
        model = Directory
        fields = ("id", "title", "alias", "description", "versions")


class DirectoryItemSerializer(serializers.ModelSerializer):
    """
    Сериалайзер элемента справочника
    """
    directory = serializers.HyperlinkedRelatedField(view_name="directory-detail", read_only=True)

    class Meta:
        model = DirectoryItem
        fields = ("id", "code", "value", "directory")


class DirectoryItemsValidateSerializer(serializers.Serializer):
    """
    Сериалайзер запроса на валидацию элементов справочника
    """
    codes = serializers.ListField(
        child=serializers.CharField(max_length=100),
        allow_empty=False,
    )
