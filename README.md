E-Commerce Website
===================

This is a fully functional e-commerce website built using Django for the backend and Bootstrap for the frontend. The website includes features such as product listings, a shopping cart, and a checkout system.

Features
--------
- Product Listings: Display products with images, descriptions, and prices.
- Shopping Cart: Add, remove, and update items in the cart.
- Checkout System: Proceed to checkout with the items in the cart.
- Responsive Design: Built with Bootstrap for a mobile-friendly experience.
- Local Storage: Cart data is stored in the browser's local storage.

Technologies Used
-----------------
- Backend: Django
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: SQLite (default Django database)
- Libraries:
  - jQuery
  - Popper.js
  - Bootstrap

Installation
------------
1. Clone the repository:
   git clone https://github.com/your-username/ecommerce-website.git
   cd ecommerce-website

2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  (On Windows: venv\Scripts\activate)

3. Install the required dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate

5. Run the development server:
   python manage.py runserver

6. Open your browser and navigate to:
   http://127.0.0.1:8000/

File Structure
--------------
ecommerce/
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py

Usage
-----
Adding Products to the Cart:
- Click the "AddToCart" button to add a product to the cart.
- The cart icon will update with the number of items in the cart.

Viewing the Cart:
- Click the cart icon to view the items in the cart.
- The cart uses a Bootstrap popover to display the items.

Updating the Cart:
- Use the "+" and "-" buttons to increase or decrease the quantity of items in the cart.

Clearing the Cart:
- Click the "Clear Cart" button to remove all items from the cart.

Scripts
-------
JavaScript Features:
- Cart Management: Handles adding, removing, and updating items in the cart.
- Popover Initialization: Uses Bootstrap's popover for the cart display.
- Local Storage: Stores cart data in the browser's local storage.

Known Issues
------------
- Ensure that jQuery and Bootstrap are loaded in the correct order to avoid errors like "Uncaught ReferenceError: $ is not defined".
- If the popover does not work, ensure that the "data-bs-toggle='popover'" attribute is added to the cart button.

Contributing
------------
Contributions are welcome! Please fork the repository and submit a pull request.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
-------
For any inquiries, please contact:
- Name: Your Name
- Email: your-email@example.com
- GitHub: https://github.com/your-username
