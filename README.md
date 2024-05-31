# Introduction

**Social Network API** is a Django Rest Framework (DRF) API for a social networking application.

- User signup and login functionality
- Search users by email and name
- Send, accept, and reject friend requests
- List friends and pending friend requests
- Rate limit on sending friend requests (max 3 per minute)


## Dependencies

- Django
- Django Rest Framework
- djangorestframework-simplejwt
- drf-ratelimit

You can install these dependencies using `pip install -r requirements.txt`.


### Steps to Create `social_network_db` Database in MySQL

1. **Access MySQL:**

   Open a terminal or command prompt and log in to MySQL with the root user or a user with sufficient privileges to create databases:
   ```bash
   mysql -u root -p
   ```

2. **Create Database:**

   Once you are logged in to MySQL, you can create the `social_network_db` database using the following command:
   ```sql
   CREATE DATABASE social_network_db;
   ```


## Installation

**1️⃣ Clone the repository**  


```
git clone https://github.com/rockposedon/social_network.git
cd social_network
```

**2️⃣ Activate virtual environment**

#### For Linux/Ubuntu, use
```
source venv/bin/activate  
```
#### For Windows, use 

```
venv\Scripts\activate 
```

**3️⃣ Install required dependencies:**


```
pip install -r requirements.txt
```
Run the command and follow the prompts to create a superuser(Initially hit requests with superuser credentials in Postman):
```
python manage.py createsuperuser
```

**4️⃣ Apply database migrations**

```
python manage.py migrate
```
**5️⃣ Run the development server**

```
python manage.py runserver
```
The API will be accessible at http://localhost:8000/

**6️⃣ API Endpoints**
```
User Authentication:
/api/signup/: User signup endpoint.
/api/login/: User login endpoint.
User Management:
/api/search/: Search users by email or name.
/api/friend-request/: Send friend request.
/api/friend-request/<int:pk>/accept/: Accept friend request.
/api/friend-request/<int:pk>/reject/: Reject friend request.
/api/friends/: List friends.
/api/pending-requests/: List pending friend requests.
```
The Signup API will be accessible at http://localhost:8000/api/signup/

**Docker**

Run Docker Compose to build and start the containers:
```
docker-compose up --build
```
The API will be accessible at http://localhost:8000/

### Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---
