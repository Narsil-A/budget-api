from rest_framework import viewsets
from rest_framework import authentication, permissions
# models and serializers 
from .models import Expense, Income, Budget
from .serializers import ExpenseSerializer, IncomeSerializer, BudgetSerializer


"""
View to handle HTTP requests and responses
"""

class ExpenseViewSet(viewsets.ModelViewSet):

    """ This class inherits from GenericAPIView and includes implementations for various actions,
    by mixing in the behavior of the various mixin classes: 
    .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
    

class IncomeViewSet(viewsets.ModelViewSet):

    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
   

class BudgetViewSet(viewsets.ModelViewSet):

    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
    