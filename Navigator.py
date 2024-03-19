from tkinter import Tk, Label, Entry, Button, Text, Scrollbar
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class Hospital:
    def __init__(self, name, address, services, ratings, costs):
        self.name = name
        self.address = address
        self.services = services
        self.ratings = ratings
        self.costs = costs

def recommend_hospitals(user_location, procedure, max_cost):
    hospitals_data = [
        Hospital("Hospital A", "New York, NY", ["Heart Surgery", "General Surgery"], 4.5, 5000),
        Hospital("Hospital B", "Los Angeles, CA", ["Heart Surgery", "Orthopedics"], 4.8, 7000),
        # Add more hospitals with their data
    ]

    recommended_hospitals = []
    geolocator = Nominatim(user_agent="hospital_recommendation")

    for hospital in hospitals_data:
        if procedure in hospital.services and hospital.costs <= max_cost:
            location = geolocator.geocode(hospital.address)
            if location:
                hospital_location = (location.latitude, location.longitude)
                distance = geodesic(user_location, hospital_location).kilometers
                recommended_hospitals.append((hospital, distance))

    recommended_hospitals.sort(key=lambda x: x[1])

    return recommended_hospitals

def get_recommendations():
    user_location = (float(entry_latitude.get()), float(entry_longitude.get()))
    procedure = entry_procedure.get()
    max_cost = float(entry_max_cost.get())

    recommended_hospitals = recommend_hospitals(user_location, procedure, max_cost)
    text_recommendations.delete(1.0, "end")

    for hospital, distance in recommended_hospitals:
        text_recommendations.insert("end", f"{hospital.name} - Distance: {distance} kilometers - Cost: ${hospital.costs}\n")

# GUI setup
root = Tk()
root.title("Hospital Recommendation System")

label_latitude = Label(root, text="Latitude:")
label_latitude.pack()
entry_latitude = Entry(root)
entry_latitude.pack()

label_longitude = Label(root, text="Longitude:")
label_longitude.pack()
entry_longitude = Entry(root)
entry_longitude.pack()

label_procedure = Label(root, text="Procedure:")
label_procedure.pack()
entry_procedure = Entry(root)
entry_procedure.pack()

label_max_cost = Label(root, text="Max Cost:")
label_max_cost.pack()
entry_max_cost = Entry(root)
entry_max_cost.pack()

button_recommend = Button(root, text="Recommend Hospitals", command=get_recommendations)
button_recommend.pack()

text_recommendations = Text(root, height=10, width=50)
text_recommendations.pack()

scrollbar = Scrollbar(root, command=text_recommendations.yview)
scrollbar.pack(side="right", fill="y")
text_recommendations.config(yscrollcommand=scrollbar.set)

root.mainloop()
