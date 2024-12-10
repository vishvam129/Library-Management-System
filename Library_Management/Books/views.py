from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book, Members, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from datetime import date, timedelta
from rest_framework.exceptions import NotFound

#  Book Management 

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save()


# Retrieve, update, or delete a specific book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Book.DoesNotExist:
            raise NotFound({"error": "The requested book does not exist."})

        self.perform_destroy(instance)  
        return Response(
            {"message": f"The book '{instance.title}' has been deleted."},
            status=status.HTTP_200_OK
        )

# Member Management 


class MemberListView(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        member_name = instance.name
        
        self.perform_destroy(instance)
        
        return Response(
            {"message": f"Member '{member_name}' has been deleted successfully."},
            status=status.HTTP_200_OK
        )

# Loan Management 

# Borrow a Book 
class LoanCreateView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.request.data.get('book')
        member_id = self.request.data.get('member')
        
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise ValueError("Invalid book ID.")
        
        try:
            member = Members.objects.get(id=member_id)
        except Members.DoesNotExist:
            raise ValueError("Invalid member ID.")

        if book.copies <= 0:
            raise ValueError("No available copies of this book.")
        
        book.copies -= 1
        book.save()

        serializer.save(borrowed_on=date.today(), due_date=date.today() + timedelta(days=14))

class LoanReturnView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        loan = self.get_object()

        if loan.returned_on:
            return Response({"error": "Book has already been returned."}, status=status.HTTP_400_BAD_REQUEST)

        loan.returned_on = date.today()

        overdue_days = (loan.returned_on - loan.due_date).days
        loan.fine = max(overdue_days * 10, 0)  
        
        book = loan.book
        book.copies += 1
        book.save()

        loan.save()
        return Response({"message": "Book returned successfully.", "fine": loan.fine}, status=status.HTTP_200_OK)

class LoanListView(generics.ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]


class LoanDetailView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

# Search Functionality 

class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)
        genre = self.request.query_params.get('genre', None)
        
        if title:
            queryset = queryset.filter(title__icontains=title)  
        if author:
            queryset = queryset.filter(author__icontains=author)  
        if genre:
            queryset = queryset.filter(genre__icontains=genre)  
        
        return queryset
