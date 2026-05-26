# recommend_doctors.py

def get_doctor_recommendations(predicted_class):
    # Dummy data (You can connect this to a real hospital API or database later)
    recommendations = {
        "Melanocytic Nevus": [
            {"name": "Dr. Priya Sharma", "rating": 4.7, "hospital": "Apollo Dermatology", "link": "https://www.apollohospitals.com"},
            {"name": "Dr. Aditya Rao", "rating": 4.5, "hospital": "Fortis Skin Care", "link": "https://www.fortishealthcare.com"},
            {"name": "Dr. Kavitha Menon", "rating": 4.6, "hospital": "KIMS Skin Centre", "link": "https://www.kimshospitals.com"},
            {"name": "Dr. Rohan Mehta", "rating": 4.4, "hospital": "AIIMS Dermatology", "link": "https://www.aiims.edu"}
        ],
        "Melanoma": [
            {"name": "Dr. Neha Verma", "rating": 4.8, "hospital": "Cancer Research Hospital", "link": "https://www.tatamemorialcentre.com"},
            {"name": "Dr. Rajesh Iyer", "rating": 4.7, "hospital": "Max Oncology", "link": "https://www.maxhealthcare.in"},
            {"name": "Dr. Anjali Sinha", "rating": 4.6, "hospital": "Apollo Cancer Institute", "link": "https://www.apollohospitals.com"},
            {"name": "Dr. Suresh Babu", "rating": 4.5, "hospital": "CMC Vellore", "link": "https://www.cmch-vellore.edu"}
        ]
        # Add more classes and doctors if needed
    }

    # Fallback if disease not listed
    default_doctors = [
        {"name": "Dr. Sneha Kapoor", "rating": 4.5, "hospital": "Global Skin Hospital", "link": "https://www.globalskinhospitals.com"},
        {"name": "Dr. Vivek Nair", "rating": 4.4, "hospital": "Apollo Dermatology", "link": "https://www.apollohospitals.com"},
        {"name": "Dr. Pooja Reddy", "rating": 4.6, "hospital": "Rainbow Skin Care", "link": "https://www.rainbowhospitals.in"},
        {"name": "Dr. Arjun Das", "rating": 4.3, "hospital": "Fortis Skin Center", "link": "https://www.fortishealthcare.com"}
    ]

    return recommendations.get(predicted_class, default_doctors)
