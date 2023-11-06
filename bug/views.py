from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import generics
from rest_framework.renderers import JSONRenderer
from django.views.decorators.http import require_GET


from bug.models import Bug, User, Project
from bug.serializers import BugsSerializer, UserSerializer


class UserApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BugsApiView(generics.ListAPIView):
    serializer_class = BugsSerializer
    queryset = Bug.objects.all()
    http_method_names = ['get']
    project_id = None
    user_id = None

    renderer_classes = [JSONRenderer]

    def user_exists(self, id):
        return User.objects.filter(id=id).exists()

    def project_exists(self, id):
        return Project.objects.filter(id=id).exists()

    def get(self, request, *args, **kwargs):
        print(self.request.GET.get("project_id"))
        self.project_id = self.request.GET.get("project_id")
        self.user_id = self.request.GET.get("user_id")
        if self.project_id:
            if not self.project_exists(self.project_id):
                print('project does not exit')
                return Response(status=status.HTTP_404_NOT_FOUND)
            self.queryset = self.queryset.filter(project=self.project_id)
            
        if self.user_id:
            if not self.user_exists(self.user_id):
                print('user does not exit')
                return Response(status=status.HTTP_404_NOT_FOUND)
            self.queryset = self.queryset.filter(user=self.user_id)    
            return super().get(request, *args, **kwargs)
        self.queryset = self.queryset.none()
        return super().get(request, *args, **kwargs)




