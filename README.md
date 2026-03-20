markdown
# FastAPI Backend

This is a FastAPI backend with authentication and authorization using Supabase.

## Installation

1. Install the required packages: `pip install -r requirements.txt`
2. Create a `.env` file with your Supabase credentials: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_KEY`
3. Run the server: `uvicorn main:app --host 0.0.0.0 --port 8000`

## API Endpoints

### Auth

* `POST /auth/register`: Register a new user
* `POST /auth/login`: Login an existing user
* `GET /auth/me`: Get the currently logged-in user

### Users

* `GET /users`: Get all users
* `GET /users/{user_id}`: Get a user by ID
* `PUT /users/{user_id}`: Update a user
* `DELETE /users/{user_id}`: Delete a user

### Products

* `GET /products`: Get all products
* `GET /products/{product_id}`: Get a product by ID
* `POST /products`: Create a new product
* `PUT /products/{product_id}`: Update a product
* `DELETE /products/{product_id}`: Delete a product