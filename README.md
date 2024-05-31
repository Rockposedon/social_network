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

## Installation

**1️⃣ Clone the repository**  

Clone the repository to your local machine using the following command:

```
git clone https://github.com/your-username/social-network-api.git
cd social-network-api
```

**2️⃣ Set up virtual environment**

Create and activate a virtual environment for the project:

#### For Linux/Ubuntu, use
```
python3 -m venv venv
source venv/bin/activate  
```
#### For Windows, use 

```
python3 -m venv venv
venv\Scripts\activate 
```

**3️⃣ Install dependencies**

Install required dependencies:

```
pip install -r requirements.txt
```


**4️⃣ Apply migrations**

Apply database migrations:

```
python manage.py migrate
```
**5️⃣ Run the development server**

Start the development server:

```
python manage.py runserver
```
The API will be accessible at http://localhost:8000/.

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
**Docker**

You can also run the application using Docker:

Build the Docker image:
```
docker-compose build
```
Run the Docker container:
```
docker-compose up
```
The API will be accessible at http://localhost:8000/.

**Contributing**
```Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature-name).
Create a new Pull Request.
```
License
```
This project is licensed under the MIT License - see the LICENSE file for details.
```
