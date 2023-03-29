from django.urls import path, include
from rest_framework import routers
from .views import ExpenseViewSet, IncomeViewSet, BudgetViewSet

"""
router to map the views to specific URLs
"""
router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]