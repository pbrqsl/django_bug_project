from django.shortcuts import get_list_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import generics


from bug.models import Bug, User
from bug.serializers import BugsSerializer, UserSerializer


class UserApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BugsApiView(generics.ListAPIView):
    serializer_class = BugsSerializer
    queryset = Bug.objects.all()

    project_id = None
    user_id = None

    def get(self, request, *args, **kwargs):
        print(self.request.GET.get("project_id"))
        self.project_id = self.request.GET.get("project_id")
        self.user_id = self.request.GET.get("user_id")
        if self.project_id or self.user_id:
            if self.project_id:
                self.queryset = self.queryset.filter(project=self.project_id)
                print(len(self.queryset))
            if self.user_id:
                self.queryset = self.queryset.filter(user=self.user_id)
            if len(self.queryset) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return super().get(request, *args, **kwargs)
        self.queryset = self.queryset.none()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        print(self.project_id)
        return super().get_queryset()


# Create your views here.
