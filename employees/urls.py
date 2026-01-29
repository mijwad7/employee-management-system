from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views_auth import (
    RegisterAPIView, ChangePasswordAPIView, ProfileAPIView,
    LoginTemplateView, RegisterTemplateView, ProfileTemplateView
)
from .views_form import FormSchemaAPIView, FormBuilderTemplateView
from .views_employee import (
    EmployeeListCreateAPIView, EmployeeDetailAPIView,
    EmployeeListTemplateView, EmployeeFormTemplateView
)
from . import views  # import generic views if any

urlpatterns = [
    # API endpoints
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPIView.as_view(), name='auth_register'),
    path('api/change-password/', ChangePasswordAPIView.as_view(), name='auth_change_password'),
    path('api/profile/', ProfileAPIView.as_view(), name='auth_profile'),
    path('api/form-schema/', FormSchemaAPIView.as_view(), name='api_form_schema'),
    
    path('api/employees/', EmployeeListCreateAPIView.as_view(), name='api_employee_list'),
    path('api/employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='api_employee_detail'),

    # Template views
    path('login/', LoginTemplateView.as_view(), name='login_page'),
    path('register/', RegisterTemplateView.as_view(), name='register_page'),
    path('profile/', ProfileTemplateView.as_view(), name='profile_page'),
    path('form-builder/', FormBuilderTemplateView.as_view(), name='form_builder_page'),
    
    path('employees/', EmployeeListTemplateView.as_view(), name='employee_list_page'),
    path('employees/new/', EmployeeFormTemplateView.as_view(), name='employee_create_page'),
    path('employees/<int:pk>/edit/', EmployeeFormTemplateView.as_view(), name='employee_edit_page'),
]
