from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FormSchema
from .serializers import FormSchemaSerializer
from django.views.generic import TemplateView

class FormSchemaAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # Get the latest schema, or return empty
        schema = FormSchema.objects.order_by('-created_at').first()
        if schema:
            serializer = FormSchemaSerializer(schema)
            return Response(serializer.data)
        return Response({"schema_data": []})

    def post(self, request):
        serializer = FormSchemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormBuilderTemplateView(TemplateView):
    template_name = 'employees/form_builder.html'
