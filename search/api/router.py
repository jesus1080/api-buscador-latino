from rest_framework.routers import DefaultRouter
from search.api.views import SearchApiViewSet

router_searchs = DefaultRouter()

router_searchs.register(prefix='search', basename='search', viewset=SearchApiViewSet)