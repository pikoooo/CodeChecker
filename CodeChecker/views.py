from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import User, Submissions
from .serializers import UserSerializer, SubmissionSerializer
from .utils import create_code_file, execute_code_file


def hello_world(request):
    return HttpResponse("Welcome to CodeChecker")


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubmissionViewSet(ModelViewSet):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):   #Over-riding the Post method for creating a code
        request.data["status"] = "P"
        file_name = create_code_file(request.data.get("code"), request.data.get("language"))
        language = request.data.get("language")
        output = execute_code_file(file_name, language)

        request.data["output"] = output

        return super().create(request, args, kwargs)







