

# Student Management API

Student Management API is a RESTful API designed to manage student-related operations in an educational system. The API provides functionality to efficiently handle key aspects of student data management. It supports CRUD (Create, Read, Update, Delete) operations to ensure that student information, are easy to access, update, and maintain.

This API allows users to manage student records by performing the following actions:


## Key Features

- **Create** new student profiles, including personal.

- **Retrieve** and view student information by unique identifiers (e.g., ID).

- **Update** student data such as name,  city, and email.

- **Delete** student profiles when no longer needed

- **Authentication with JWT (JSON Web Tokens)** to secure access to the API endpoints.


## API Endpoints

#### Get all items

```http
  GET /api/list (http://127.0.0.1:8000/api/list/)
```

| Parameter            | Type  | Description                | Method |
| :------------------- | :---- | :------------------------- | :----- |
| `No parameter` | `N/A` | **List**. Retrieve all students data | `GET` |


#### Get item

```http
  GET /api/items/<id>/ (http://127.0.0.1:8000/api/list/2/)
```

| Parameter            | Type  | Description                | Method |
| :------------------- | :---- | :------------------------- | :----- |
| `id` | `int` | **Required**. Id of item to fetch | `GET` |

#### Create items 

```http
  POST /api/create (http://127.0.0.1:8000/api/create/)
```

| Parameter            | Type  | Description                | Method |
| :------------------- | :---- | :------------------------- | :----- |
| `No parameter` | `N/A` | **Create**. new student records | `POST` |


#### Complete Update item

```http
  PUT /api/update/<id>/ (http://127.0.0.1:8000/api/update/1/)
```

| Parameter            | Type  | Description                | Method |
| :------------------- | :---- | :------------------------- | :----- |
| `id` | `int` | **Required**. Id of item for complete update | `PUT` |

#### Partial Update item

```http
  PATCH /api/update/<id>/ (http://127.0.0.1:8000/api/update/1/)
```

| Parameter            | Type  | Description                | Method |
| :------------------- | :---- | :------------------------- | :----- |
| `id` | `int` | **Required**. Id of item for partial update | `PATCH` |

#### Delete item

```http
  DELETE /api/destroy/<id>/ (http://127.0.0.1:8000/api/destroy/1/)
```

| Parameter            | Type  | Description                | Method |
| :------------------- | :---- | :------------------------- | :----- |
| `id` | `int` | **Required**. Id of item to delete | `DELETE` |


#### Authentication

| Endpoint               | Method | Description                        | Parameters |
|------------------------|--------|------------------------------------|------------|
| `/api/token/`           | POST   | Obtain a JWT access and refresh token | N/A        |
| `/api/refresh/token/`   | POST   | Refresh the JWT access token       | N/A        |



##  Endpoint Details

#### **1. Create a New Student Record**

- Method: POST
- Endpoint: api/create/

This action allows users to create a new student record by submitting a student's details (such as name, roll number, email, and city) via a POST request. The data is sent in JSON format, and the API will validate the input before saving the student record in the database.

#### **Request Format**
When sending a POST request, you need to provide the following data in JSON format:

```bash
{
  "name": "Sohail Ahmad",
  "roll_no": 103,
  "email": "sohailahmed34280@gmail.com",
  "city": "Karachi"
}
```

#### **Response**
If the request is valid and the data passes validation, the API will create a new student record and return the newly created record along with a 201 Created status code.

#### **2. Read (Retrieve) Student Records**

- Method: GET
- Endpoint: api/list/ (Retrieve all students)
- Endpoint: api/list/id/ (Retrieve a single student by ID)

This action allows users to read student records from the system.

#### **Request Format**
- GET /list/: No data needs to be sent, just make the GET request.
- GET /list/2/: This retrieves the student with the ID 2.


#### **Response**
The API responds with a JSON array (for all students) or a JSON object (for a specific student), along with a 202 Accepted status code.

```bash
{
  "roll_no": 2
  "name": "Sidra",
  "roll_no": 612,
  "email": "sidraqurban77@gmail.com",
  "city": "Karachi"
}
```

#### **3. Update an Existing Student Record**

- Method: PUT (Full update) or PATCH (Partial update)
- Endpoint: api/update/id/
This action allows users to update the details of an existing student:

- **PUT:** Updates all fields of the student record.
- **PATCH:** Updates only the specific fields that are provided in the request.

#### **Request Format**
- PUT /update/1/ (Full update):

```bash
{
  "name": "Sajjad Ali",
  "roll_no": 1044,
  "email": "sajjadali@gmail.com",
  "city": "Lahore"
}
```
- PATCH /update/4/ (Partial update):

```bash
{
  "name": "Ali Khan"
}
```


#### **Response**
If the update is successful, the API will return the updated student record along with a 200 OK status code

#### **4. Delete a Student Record**

- Method: DELETE
- Endpoint: api/destroy/id/

This action allows users to delete a student record by specifying the student's ID. Once deleted, the record is permanently removed from the database.

#### **Request Format**
- DELETE api/destroy/4/: Deletes the student with ID 4.


#### **Response**
If the deletion is successful, the API will return a 204 No Content status code, indicating that the resource has been deleted successfully.


#### **5. Authentication**
This API uses JWT (JSON Web Token) for secure access. To use the API endpoints, you first need to authenticate and obtain an access token by posting your credentials to /api/token/. After receiving the token, include it in the Authorization header of your requests.

##### **Steps for Authentication:**

- **Obtain Token:** Post your username and password to /api/token/ to get a JWT.
- **Access Token:** Use the access token to authenticate API requests by including it in the Authorization header.
- **Refresh Token:** If the access token expires, you can use the refresh token to get a new one via /api/refresh/token/.

#### **Request format for access token**
```bash
{
    "username": "your_username",
    "password": "your_password"
}
```
#### **Response**
```bash
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```


## Installation

1. **Clone the repository:**
    ```bash
    https://github.com/Sohail342/DRF-CRUD-API.git
    cd DRF_CRUD
    ```

2. **Create a virtual environment:** (optional but recommended)
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    **Be sure in project directory to install requirements.txt** 

4. **Make migrations:**
    ```bash
    python manage.py makemigrations
    ```

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## How to access API endpoints
You can interact with the API endpoints using various tools and methods, such as Postman, HTTPie, or even curl. Here we are going to use both postman and httpie (third party package) to interact with endpoints.

### Accessing API endpoints using HTTPie

first install the httpie (if not installed)

```bash
pip install httpie
```

**note :** before accessing API endpoints you must have;

- Run database migrations
- Create superuser or user
- Access token
- Run local server

**Hit** the following endpoint to get access token;

```bash
http POST http://127.0.0.1:8000/api/token username=your_username password=your_password
```
Replace your_username with the username you created and your_password with your password. The token generated will be valid for the user you created. By default, the access token is valid for 5 minutes, and the refresh token is valid for 1 day (these default values can be overridden).

Now you can use your access token to access student API endpoints.

**1. List the Students list**
```bash
http GET http://127.0.0.1:8000/api/list/ Authorization:"Bearer <your_token>"
```

**2. Create new Student**
```bash
http POST http://127.0.0.1:8000/api/create/ name=Sohail city=Karachi roll_no=231 Authorization:"Bearer <your_token>"
```

**3. Partial update**
```bash
http PATCH http://127.0.0.1:8000/api/update/1 name=Sidra Authorization:"Bearer <your_token>"
```

**4. Delete record**
```bash
http DELETE http://127.0.0.1:8000/api/destroy/1 Authorization:"Bearer <your_token>"
```

Once your access token is expired you may generate token again or using refresh token you generate new access token.

#### **Using Refresh token**
```bash
http POST http://127.0.0.1:8000/api/refresh/token refresh="<your_refresh_token>"
```

## Tech Stack

**Server side:** Django, Python

**RESTful API:** Dajango RESTful Framework (DRF)


## Contact

If you have any questions or feedback, feel free to reach out:

<p align="left">
<a href="https://wa.me/+923428041928" target="blank"><img align="center" src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/sohail_ahmad342" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="sohail_ahmad342" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/sohailahmad3428041928/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sohail-ahmad342" height="30" width="40" /></a>
<a href="https://instagram.com/sohail_ahmed113" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sohail_ahmed113" height="30" width="40" /></a>
<a href="mailto:sohailahmed34280@gmail.com" target="blank"><img align="center" src="https://img.icons8.com/ios-filled/50/000000/email-open.png" alt="Email" height="30" width="40" /></a>
</p>
