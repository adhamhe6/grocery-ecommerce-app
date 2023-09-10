# Django Grocery Ecommerce Website

![Project Logo](static/images/logo.png)

A comprehensive grocery ecommerce website built with Django, providing a seamless shopping experience for users. The website offers a variety of grocery products, brands, categories, and useful features such as user registration, login, logout, password change, password reset, user profile management, cart functionality, order tracking, secure payment integration, a compare list, an engaging user interface, and a blog section.

## Features

- User Registration: Allow users to create new accounts to access personalized features.
- User Login and Logout: Securely authenticate users and manage user sessions.
- Password Change: Enable users to update their account passwords.
- Password Reset: Provide a password recovery mechanism for users.
- User Profile: Allow users to manage their profile information.
- Product Catalog: Display a wide range of grocery products, brands, and categories.
- Cart Functionality: Enable users to add/remove products to/from their cart and manage quantities.
- Order Tracking: Allow users to track the status of their orders.
- Secure Payment Integration: Integrate a secure payment gateway for seamless transactions.
- Compare List: Enable users to compare products side by side.
- Engaging UI: Provide an intuitive and visually appealing user interface.
- Blog: Offer a blog section to share news, updates, and informative articles.

## Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/your-repo.git
```
2. Create and activate a virtual environment:

```shell
python -m venv env
source env/bin/activate
```
3. Install the dependencies:

```shell
pip install -r requirements.txt
```
4. Set up the database:

```shell
python manage.py migrate
```
5. Create a superuser account:

```shell
python manage.py createsuperuser
```
6. Start the development server:

```shell
python manage.py runserver
```
7. Access the website at http://localhost:8000.

## Configuration
- Database: The project uses the default SQLite database for development. For production, consider using a more robust database system such as PostgreSQL or MySQL.

- Payment Gateway Integration: Configure the payment gateway credentials in the appropriate settings file (`settings.py`).

## Usage
1. Go to the website homepage and explore the product catalog.
2. Register a new account or log in to an existing account.
3. Add products to your cart and manage quantities.
4. Proceed to the checkout page and complete the payment process.
5. Track the status of your orders in the order tracking section.
6. Explore the blog section for news, updates, and informative articles.

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or new features to propose, please open an issue or submit a pull request.

## License
MIT License