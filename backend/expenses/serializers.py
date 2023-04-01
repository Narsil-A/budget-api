from rest_framework import serializers
from .models import Expense, Income, Budget

"""
Serializers to convert the model objects to JSON format
"""


class ExpenseSerializer(serializers.ModelSerializer):
    """
    provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields
    """
    
    class Meta:
        model = Expense
        fields = '__all__'  # to indicate that all fields in the model should be used

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'