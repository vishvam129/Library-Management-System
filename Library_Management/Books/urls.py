from django.urls import path, include
from .views import (
    BookListView, BookDetailView,
    MemberListView, MemberDetailView,
    LoanCreateView, LoanReturnView,
    LoanListView, LoanDetailView,
    BookSearchView
)



urlpatterns = [
    # Book Management
    path('books/', BookListView.as_view(), name='book-list'),  
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), 

    # Member Management
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'), 

    # Loan Management
    path('loans/', LoanCreateView.as_view(), name='loan-create'),  
    path('loans/return/<int:pk>/', LoanReturnView.as_view(), name='loan-return'), 
    path('loans_all/', LoanListView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'), 

    # Search Functionality
    path('books/search/', BookSearchView.as_view(), name='book-search'), 
]
