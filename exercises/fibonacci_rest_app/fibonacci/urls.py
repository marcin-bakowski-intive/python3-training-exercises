from django.urls import path

from fibonacci import views


urlpatterns = [
    path('fibonacci/', views.FibonacciNumbersView.as_view(), name="fibonacci"),
    path('fibonacci/<int:n>/', views.FibonacciNumbersNInPathView.as_view(), name="fibonacci_n_in_path"),
]
