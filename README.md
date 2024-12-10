# Library Management System


## **Create Superuser for Authentication**

Before implementing authentication for your API, you need to create a **superuser** in Django.
---

## **Steps to Create a Superuser**

### **1. Run the Superuser Creation Command**

In your terminal, run the following command:
```bash
python manage.py createsuperuser
```

---

### **2. Enter the Required Information**

When prompted, enter the following details:

1. **Username**: Choose a unique username for the superuser.
2. **Email Address**: Provide a valid email address for the superuser.
3. **Password**: Enter a strong password and confirm it.

#### **Example Input**
```plaintext
Username (leave blank to use 'admin'): admin_user
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

---

## **Authentication**

### **Overview**
To access certain features of the API, users must authenticate themselves. This is done using **Token Authentication**. Users can obtain an authentication token by providing valid credentials (`username` and `password`) and then use this token to access protected endpoints.

### **Endpoints**

#### **1. Obtain Authentication Token**
- **URL**: `/api-token-auth/`
- **Method**: `POST`
- **Description**: Authenticate the user and obtain a token.

##### **Request Example**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

##### **Response Example**
```json
{
  "token": "your_token_value"
}
```

##### **Usage**
Include the obtained token in the `Authorization` header for protected requests:
```
Authorization: Token your_token_value
```

---

## **Book Management**

### **Overview**
The **Book Management API** allows users to:
- Retrieve a list of all books (public access).
- Retrieve details of a specific book
- Add a new book to the inventory (requires authentication).
- Update book details (requires authentication).
- Remove a book from the inventory (requires authentication).

### **Endpoints**

---

### **1. Retrieve All Books**
- **URL**: `/api/books/`
- **Method**: `GET`
- **Authentication**: Not required.
- **Description**: Returns a list of all books.

##### **Response Example**
```json
[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "genre": "Fiction",
    "copies": 10
  },
  {
    "id": 2,
    "title": "Another Book",
    "author": "Another Author",
    "genre": "Science",
    "copies": 5
  }
]
```

---

### **2. Add a New Book**
- **URL**: `/api/books/`
- **Method**: `POST`
- **Authentication**: Required.
- **Description**: Allows authenticated users to add a new book to the inventory.

##### **Request Example**
```json
{
  "title": "New Book Title",
  "author": "Author Name",
  "genre": "Non-Fiction",
  "copies": 5
}
```

##### **Response Example**
```json
{
  "id": 3,
  "title": "New Book Title",
  "author": "Author Name",
  "genre": "Non-Fiction",
  "copies": 5
}
```

---

### **3. Retrieve Details of a Specific Book**
- **URL**: `/api/books/<int:id>/`
- **Method**: `GET`
- **Authentication**: Not required.
- **Description**: Retrieves details of a specific book by its ID.

##### **Response Example**
```json
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "genre": "Fiction",
  "copies": 10
}
```

---

### **4. Update Book Details**
- **URL**: `/api/books/<int:id>/`
- **Method**: `PATCH`
- **Authentication**: Required.
- **Description**: Allows authenticated users to update specific details of a book.

##### **Request Example**
```json
{
  "copies": 3
}
```

##### **Response Example**
```json
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "genre": "Fiction",
  "copies": 3
}
```

---

### **5. Delete a Book**
- **URL**: `/api/books/<int:id>/`
- **Method**: `DELETE`
- **Authentication**: Required.
- **Description**: Deletes a book from the inventory.

##### **Response Example**
```json
{
  "message": "The book 'Book Title' has been deleted."
}
```

---


---

# **Member Management API Documentation**

The Member Management API allows you to perform the following actions:

1. Retrieve a list of all members (requires authentication).
2. Retrieve details of a specific member (requires authentication).
3. Register a new member (requires authentication).
4. Update an existing member's details (requires authentication).
5. Remove a member (requires authentication).

---

## **Endpoints**

### **1. Retrieve All Members**
- **URL**: `/api/members/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Token <your_token>`
- **Description**: Retrieves a list of all registered members. Authentication is required.

#### **Example Request**
```bash
curl -X GET http://127.0.0.1:8000/api/members/ \
-H "Authorization: Token <your_token>"
```

#### **Example Response**
```json
[
    {
        "id": 1,
        "name": "user",
        "email": "user@example.com",
        "phone_number": "1234567890",
        "address": "Gandhinagar",
        "membership_date": "2024-12-09"
    },
    {
        "id": 2,
        "name": "user1",
        "email": "user1@example.com",
        "phone_number": "9876543210",
        "address": "Gandhinagar",
        "membership_date": "2024-12-10"
    }
]
```

---

### **2. Retrieve Details of a Specific Member**
- **URL**: `/api/members/<id>/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Token <your_token>`
- **Description**: Retrieves the details of a specific member by their ID. Authentication is required.

#### **Example Request**
```bash
curl -X GET http://127.0.0.1:8000/api/members/1/ \
-H "Authorization: Token <your_token>"
```

#### **Example Response**
```json
{
    "id": 1,
    "name": "user",
    "email": "user@example.com",
    "phone_number": "1234567890",
    "address": "Gandhinagar",
    "membership_date": "2024-12-09"
}
```

---

### **3. Register a New Member**
- **URL**: `/api/members/`
- **Method**: `POST`
- **Headers**:
  - `Authorization: Token <your_token>`
  - `Content-Type: application/json`
- **Description**: Registers a new member in the system. Authentication is required.

#### **Request Body**
```json
{
    "name": "user",
    "email": "user@example.com",
    "phone_number": "1231231234",
    "address": "Gandhinagar"
}
```

#### **Example Request**
```bash
curl -X POST http://127.0.0.1:8000/api/members/ \
-H "Authorization: Token <your_token>" \
-H "Content-Type: application/json" \
-d '{
    "name": "user",
    "email": "user@example.com",
    "phone_number": "1231231234",
    "address": "Gandhinagar"
}'
```

#### **Example Response**
```json
{
    "id": 3,
    "name": "user",
    "email": "user@example.com",
    "phone_number": "1231231234",
    "address": "Gandhinagar",
    "membership_date": "2024-12-10"
}
```

---

### **4. Update Member Details**
- **URL**: `/api/members/<id>/`
- **Method**: `PATCH`
- **Headers**:
  - `Authorization: Token <your_token>`
  - `Content-Type: application/json`
- **Description**: Updates details of a specific member. Authentication is required.

#### **Request Body**
You only need to include the fields you want to update:
```json
{
    "phone_number": "1112223333",
    "address": "Amd"
}
```

#### **Example Request**
```bash
curl -X PATCH http://127.0.0.1:8000/api/members/1/ \
-H "Authorization: Token <your_token>" \
-H "Content-Type: application/json" \
-d '{
    "phone_number": "1112223333",
    "address": "Amd"
}'
```

#### **Example Response**
```json
{
    "id": 1,
    "name": "user",
    "email": "user@example.com",
    "phone_number": "1112223333",
    "address": "Amd",
    "membership_date": "2024-12-09"
}
```

---

### **5. Remove a Member**
- **URL**: `/api/members/<id>/`
- **Method**: `DELETE`
- **Headers**:
  - `Authorization: Token <your_token>`
- **Description**: Deletes a member by their ID. Authentication is required.

#### **Example Request**
```bash
curl -X DELETE http://127.0.0.1:8000/api/members/1/ \
-H "Authorization: Token <your_token>"
```

#### **Example Response**
```json
{
    "message": "Member 'user' has been deleted successfully."
}
```

---

---

# **Loan Management API Documentation**

The Loan Management API allows you to:

1. Borrow a book (requires authentication).
2. Return a book (requires authentication).
3. Retrieve all loans (requires authentication).
4. Retrieve details of a specific loan (requires authentication).

---

## **Endpoints**

### **1. Borrow a Book**
- **URL**: `/api/loans/`
- **Method**: `POST`
- **Headers**:
  - `Authorization: Token <your_token>`
  - `Content-Type: application/json`
- **Description**: Creates a new loan for borrowing a book. The request must include the `book_id` and `member_id`.

#### **Request Body**
```json
{
    "book": 1,
    "member": 1
}
```

#### **Example Request**
```bash
curl -X POST http://127.0.0.1:8000/api/loans/ \
-H "Authorization: Token <your_token>" \
-H "Content-Type: application/json" \
-d '{
    "book": 1,
    "member": 1
}'
```

#### **Example Response**
```json
{
    "id": 1,
    "book": 1,
    "member": 1,
    "borrowed_on": "2024-12-09",
    "due_date": "2024-12-23",
    "returned_on": null,
    "fine": 0.0
}
```

---

### **2. Return a Book**
- **URL**: `/api/loans/return/<loan_id>/`
- **Method**: `POST`
- **Headers**:
  - `Authorization: Token <your_token>`
  - `Content-Type: application/json`
- **Description**: Marks a loan as returned, calculates any overdue fine, and updates the `returned_on` date.

#### **Request Body**
No request body is required.

#### **Example Request**
```bash
curl -X POST http://127.0.0.1:8000/api/loans/return/1/ \
-H "Authorization: Token <your_token>"
```

#### **Example Response**
```json
{
    "message": "Book returned successfully.",
    "fine": 4
}
```

---

### **3. Retrieve All Loans**
- **URL**: `/api/loans_all/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Token <your_token>`
- **Description**: Retrieves a list of all loan records.

#### **Example Request**
```bash
curl -X GET http://127.0.0.1:8000/api/loans_all/ \
-H "Authorization: Token <your_token>"
```

#### **Example Response**
```json
[
    {
        "id": 1,
        "book": 1,
        "member": 1,
        "borrowed_on": "2024-12-09",
        "due_date": "2024-12-23",
        "returned_on": null,
        "fine": 0.0
    },
    {
        "id": 2,
        "book": 2,
        "member": 2,
        "borrowed_on": "2024-12-01",
        "due_date": "2024-12-15",
        "returned_on": "2024-12-16",
        "fine": 2
    }
]
```

---

### **4. Retrieve Details of a Specific Loan**
- **URL**: `/api/loans/<loan_id>/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Token <your_token>`
- **Description**: Retrieves the details of a specific loan.

#### **Example Request**
```bash
curl -X GET http://127.0.0.1:8000/api/loans/1/ \
-H "Authorization: Token <your_token>"
```

#### **Example Response**
```json
{
    "id": 1,
    "book": 1,
    "member": 1,
    "borrowed_on": "2024-12-09",
    "due_date": "2024-12-23",
    "returned_on": null,
    "fine": 0.0
}
```

---

# **Search for Books by Title, Author, and Genre API Documentation**

The **Search for Books API** allows users to search for books based on the following criteria:
- **Title**
- **Author**
- **Genre**
- Combination of all parameters

The API supports **query parameters** for filtering the results.

---

## **Endpoint**

- **URL**: `/api/books/search/`
- **Method**: `GET`
- **Description**: Retrieve books filtered by **title**, **author**, **genre**, or any combination of these.

---

## **Query Parameters**

You can filter books using the following query parameters:

- **`title`** *(optional)*: Filter books by title (partial or full matches allowed).
- **`author`** *(optional)*: Filter books by author name (partial or full matches allowed).
- **`genre`** *(optional)*: Filter books by genre (partial or full matches allowed).

You can combine multiple parameters to refine your search.

---

## **Request Example**

### **1. Search by Title**


- **Request**:
  ```bash
  GET /api/books/search/?title=Book
  ```

- **Example cURL Request**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/books/search/?title=Book"
  ```

- **Example Response**:
  ```json
  [
      {
          "id": 1,
          "title": "Book",
          "author": "Author",
          "genre": "Science",
          "copies": 5
      }
  ]
  ```

---

### **2. Search by Author**


- **Request**:
  ```bash
  GET /api/books/search/?author=Author
  ```

- **Example cURL Request**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/books/search/?author=Author"
  ```

- **Example Response**:
  ```json
  [
      {
          "id": 1,
          "title": "Book",
          "author": "Author",
          "genre": "Science",
          "copies": 5
      }
  ]
  ```

---

### **3. Search by Genre**


- **Request**:
  ```bash
  GET /api/books/search/?genre=Science
  ```

- **Example cURL Request**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/books/search/?genre=Science"
  ```

- **Example Response**:
  ```json
  [
     {
          "id": 1,
          "title": "Book",
          "author": "Author",
          "genre": "Science",
          "copies": 5
      }
  ]
  ```

---

### **4. Search by Multiple Criteria (Title, Author, and Genre)**


- **Request**:
  ```bash
  GET /api/books/search/?title=Book&author=Author&genre=Science
  ```

- **Example cURL Request**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/books/search/?title=Book&author=Author&genre=Science"
  ```

- **Example Response**:
  ```json
  [
     {
          "id": 1,
          "title": "Book",
          "author": "Author",
          "genre": "Science",
          "copies": 5
      }
  ]
  ```

---

### **5. No Matching Results**

If no books match the search criteria, the API will return an empty array.

- **Example Response**:
  ```json
  []
  ```
