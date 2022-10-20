from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    # filterset_fields = ['creator', ]
    filterset_class = AdvertisementFilter
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return Advertisement.objects.all()
        elif self.request.user.is_anonymous:
            return Advertisement.objects.exclude(status='DRAFT')
        else:
            return Advertisement.objects.filter(Q(status='CLOSED') | Q(status='OPEN') |
                                                Q(creator=self.request.user) &
                                                Q(status='DRAFT'))

    # Проверку на права дейсвий прописал в permissions.py
    #
    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []


