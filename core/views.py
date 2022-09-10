from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import comment



class CommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        comments = comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
