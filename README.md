# Project Description
Django-based RESTful API with OpenID Connect Authentication. 
Designed a simple customers and orders database management.

## Technologies Used
- Framework: Python Django with Django Rest Framework
- Database: PostgreSQL
- Authentication: Google OAuth2 with OpenID Connect
- Africa’s Talking SMS Gateway

## Getting Started

### Instructions on how to set up and run the project locally.
```
git clone https://github.com/rkipchumba/Savannah-Backend-Test
cd Savannah-Backend-Test
```

- Create Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

- Install Dependencies
```
pip install -r requirements.txt
```

- Database Configuration
Update the database settings in `settings.py` with your PostgreSQL credentials
```
Apply Migrations:- 
python manage.py migrate
```

- Create Superuser for admin access
```
python manage.py createsuperuser
```
- Google OAuth2 Configuration:
Set up the Google OAuth2 credentials in your project's settings

- Run the Server
```
python manage.py runserver
```

- Access the Application
```
http://127.0.0.1:8000/
```
- Testing
```
python manage.py test
```




## API Endpoints
### Create a New Customer
- Method: POST
- Endpoint: http://127.0.0.1:8000/api/customers/
```
Request Body: JSON object with customer details
Headers: [{"key":"Content-Type","value":"application/json"]
sample Body
{
  "customer": 1,
  "item": "Spoon",
  "amount": 50.00,
  "time": "2024-02-12T12:00:00Z"
}
```

## Authentication and Authorization

Explain how authentication and authorization work in my project.

## SMS Integration

Details on how SMS integration with Africa’s Talking works.

## Testing

Information on the testing strategy and how to run tests.

## CI/CD Pipeline

Overview of the CI/CD workflow using GitHub Actions.

## Web Security 

Implemented Content Security Policy (Cross-Site Scripting(XSS) headers 
to restrict the types of content that can be loaded on the web pages. 
This can help prevent malicious script execution.


