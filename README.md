# Project Description
Django RESTful API featuring OpenID Connect Authentication. Developed a database management system for customers and orders. Users to seamlessly create customers, obtain unique customer IDs, and initiate order creation. Customers can effortlessly place orders and receive instant confirmation messages, ensuring a smooth and efficient process.

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
Django's testing framework that makes it easy to create and 
run tests was implemented. 
The coverage package is used to measure code coverage
```
python manage.py test
```
For a nicer presentation, use `coverage html` Then open htmlcov/index.html in your browser, to see a report.




## API Endpoints
### Create a New Order
- Method: POST
- Endpoint: http://127.0.0.1:8000/api/orders/
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
### Create a New Customer
- Method: POST
- Endpoint: http://127.0.0.1:8000/api/Customers/
```
Request Body: JSON object with order details
Headers: [{"key":"Content-Type","value":"application/json"]
sample Body
{
  "name": "John Doe",
  "code": "JD001"
}
```


### Retrieve List of Customers
- Method: GET
- Endpoint: http://127.0.0.1:8000/api/customers/

### Retrieve List of Orders
- Method: GET
- Endpoint: http://127.0.0.1:8000/api/orders/

### Retrieve Single Customer
- Method: GET
- Endpoint: http://127.0.0.1:8000/api/<customer_id>/

### Retrieve Single Order 
- Method: GET
- Endpoint: http://127.0.0.1:8000/api/<order_id>/

## SMS Integration

 When an order is added, the customer receives an SMS alerting them they
 have placed an order from M-Savannah (custom sender ID ).
 I used the Africa’s Talking SMS gateway and sandbox. Set up USERNAME and API_KEY
`https://developers.africastalking.com/`

![Sample SMS Response in Africa’s Talking Simulator ](customers_orders/img/sms_test.png)



## Authentication and Authorization

Explain how authentication and authorization work in my project.


## CI/CD Pipeline

The projects uses  GitHub Actions workflow for simplicity. The workflow 
ensures that the project can be successfully built and that tests are executed, 
providing coverage information. The PostgreSQL service is used in the CI 
process, and health checks ensures its availability during the workflow

## Web Security 

Implemented Content Security Policy (Cross-Site Scripting(XSS) headers 
to restrict the types of content that can be loaded on the web pages. 
This can help prevent malicious script execution.


