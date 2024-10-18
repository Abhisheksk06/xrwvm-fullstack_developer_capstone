from .models import CarMake, CarModel, Dealer

def initiate():
    # Create Dealer instances
    dealer_data = [
        {"name": "Dealer A", "location": "Location A", "contact": "1234567890"},
        {"name": "Dealer B", "location": "Location B", "contact": "0987654321"},
    ]

    dealer_instances = []
    for data in dealer_data:
        dealer_instances.append(Dealer.objects.create(
            name=data['name'],
            location=data['location'],
            contact=data['contact']
        ))

    # Create CarMake instances
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    # Create CarModel instances with the corresponding CarMake and Dealer instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer": dealer_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer": dealer_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer": dealer_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer": dealer_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer": dealer_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer": dealer_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer": dealer_instances[0]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer": dealer_instances[0]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer": dealer_instances[0]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer": dealer_instances[1]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer": dealer_instances[1]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "dealer": dealer_instances[0]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer": dealer_instances[1]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer": dealer_instances[1]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "dealer": dealer_instances[0]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            dealer=data['dealer'],  # Pass the dealer instance here
            type=data['type'],
            year=data['year']
        )
