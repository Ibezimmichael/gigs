from rest_framework import generics, mixins
from .models import Gig
from .serializers import GigSerializer
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model


class GigListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """
    a view for creating and listing gigs
    """
    serializer_class = GigSerializer
    queryset = Gig.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
        return super().perform_create(serializer)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GigRetrieveUpdateDeleteView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    serializer_class = GigSerializer
    queryset = Gig.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



User = get_user_model()

class ListGigsForUser(ListAPIView):
    serializer_class = GigSerializer
    def get_queryset(self):
        username = self.kwargs.get('user')
        user = User.objects.get(username=username)
        queryset = Gig.objects.filter(created_by=user)
        return queryset
