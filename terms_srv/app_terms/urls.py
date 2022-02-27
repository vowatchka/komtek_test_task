from django.urls import path
from rest_framework import routers

from .api import DirectoryApiView, DirectoryItemApiView

router = routers.DefaultRouter()
router.register("directories", DirectoryApiView)

urlpatterns = router.urls

urlpatterns += [
    path("directories/<int:directory_pk>/items/", DirectoryItemApiView.as_view({"get": "list"}),
         name="directory-items-list"),
    path("directories/<int:directory_pk>/items/<int:pk>/", DirectoryItemApiView.as_view({"get": "retrieve"}),
         name="directory-items-detail"),
    path("directories/<int:directory_pk>/items/validate/", DirectoryItemApiView.as_view({"post": "validate"}),
         name="directory-items-validate"),
]
