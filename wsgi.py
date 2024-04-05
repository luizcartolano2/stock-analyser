"""Docstring for the wsgi.py module.

"""
from src.app import create_app


if __name__ == "__main__":
    # Create the Flask app using the create_app function
    app = create_app()
    app.run()
