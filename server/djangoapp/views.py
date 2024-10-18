# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from datetime import datetime
from .models import CarMake, CarModel, Dealer, Review
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    
    # Try to check if provided credentials can be authenticated
    user = authenticate(username=username, password=password)
    if user is not None:
        # If user is valid, call login method to log in current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    else:
        data = {"userName": username, "status": "Unauthenticated"}
    
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"status": "Logged out"})

def get_cars(request):
    count = CarModel.objects.count()  # Count of car models
    if count == 0:
        initiate()  # Populate the database if empty

    car_models = CarModel.objects.select_related('car_make')  # Fetch car models with related car makes
    cars = []
    
    for car_model in car_models:
        # Append the car details to the cars list
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name,
            "Type": car_model.type,
            "Year": car_model.year,
        })
    
    # Return the count and car details in the response
    return JsonResponse({"count": count, "cars": cars})

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    # Implementation for user registration
    pass

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    # Implementation for getting dealerships
    pass

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    # Implementation for getting dealer reviews
    pass

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    # Implementation for getting dealer details
    pass

# Create a `add_review` view to submit a review
def add_review(request):
    # Implementation for adding a review
    pass
