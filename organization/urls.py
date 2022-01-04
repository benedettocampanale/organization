from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, serializers, viewsets
from salary.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date',
        ]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()


router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet, basename='question')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
