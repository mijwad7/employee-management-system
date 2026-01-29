from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer
from django.views.generic import TemplateView

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Employee.objects.all()
        # Search Implementation
        # 1. Generic Search (?search=value)
        search_query = self.request.query_params.get('search', None)
        if search_query:
            # Search in name, email
            q = Q(name__icontains=search_query) | Q(email__icontains=search_query)
            queryset = queryset.filter(q)

        # 2. Dynamic Field Filtering (?Label=Value)
        reserved = ['search', 'page', 'limit']
        for key, value in self.request.query_params.items():
            if key not in reserved:
                kwargs = {f"dynamic_data__{key}__icontains": value}
                queryset = queryset.filter(**kwargs)
        
        return queryset.order_by('-created_at')

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

# Template Views

class EmployeeListTemplateView(TemplateView):
    template_name = 'employees/employee_list.html'

class EmployeeFormTemplateView(TemplateView):
    template_name = 'employees/employee_form.html'
