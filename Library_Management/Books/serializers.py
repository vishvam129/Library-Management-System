from rest_framework import serializers
from .models import Book, Members, Loan

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

from datetime import  datetime

class MemberSerializer(serializers.ModelSerializer):
    membership_date = serializers.SerializerMethodField()

    class Meta:
        model = Members
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'membership_date']

    def get_membership_date(self, obj):
        if isinstance(obj.membership_date, datetime):
            return obj.membership_date.date()
        return obj.membership_date
    
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
