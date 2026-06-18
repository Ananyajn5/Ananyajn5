from django.shortcuts import render

def home(request):
    return render(request, "planner/home.html")


def recommend(request):

    destination = request.GET.get('destination')
    budget = int(request.GET.get('budget', 0))

    # destination images
    image = f"https://source.unsplash.com/800x400/?{destination},travel"

    # hotel database
    hotels_data = [
        {"name": "Luxury Resort", "price": 15000},
        {"name": "Comfort Hotel", "price": 8000},
        {"name": "Budget Stay", "price": 4000},
    ]

    hotels = [h for h in hotels_data if h["price"] <= budget]

    # places database
    places_data = [
        {"name": "Beach", "price": 1000},
        {"name": "Museum", "price": 500},
        {"name": "City Tour", "price": 1500},
        {"name": "Temple Visit", "price": 300},
    ]

    places = [p for p in places_data if p["price"] <= budget]

    # AI itinerary
    itinerary = [
        f"Day 1: Arrival in {destination}, explore local markets",
        f"Day 2: Visit famous attractions in {destination}",
        f"Day 3: Relaxation and shopping before departure"
    ]

    context = {
        "destination": destination,
        "budget": budget,
        "hotels": hotels,
        "places": places,
        "image": image,
        "itinerary": itinerary
    }

    return render(request, "planner/recommend.html", {
    "destination": destination,
    "budget": budget,
    "hotels": hotels,
    "places": places,
    "image": image,
    "itinerary": itinerary
})

