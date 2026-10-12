from django.shortcuts import render

CLASSES = [
    {"name": "HIIT Blast", "icon": "bi-fire", "time": "Mon & Wed · 6:00 AM", "level": "Intermediate",
     "desc": "45 minutes of high-intensity intervals to burn fat and build stamina."},
    {"name": "Power Yoga", "icon": "bi-flower1", "time": "Tue & Thu · 7:00 AM", "level": "All levels",
     "desc": "Flow, stretch and breathe. Great for flexibility and stress relief."},
    {"name": "Strength Lab", "icon": "bi-trophy-fill", "time": "Mon – Fri · 5:30 PM", "level": "All levels",
     "desc": "Learn proper lifting form with coach-led barbell and dumbbell sessions."},
    {"name": "Spin Cycle", "icon": "bi-bicycle", "time": "Sat · 8:00 AM", "level": "Beginner",
     "desc": "Music-driven indoor cycling that torches calories and lifts your mood."},
    {"name": "Boxing Fit", "icon": "bi-bullseye", "time": "Fri · 6:30 PM", "level": "Intermediate",
     "desc": "Pads, bags and footwork. No fighting experience needed."},
    {"name": "Kids Active", "icon": "bi-emoji-smile-fill", "time": "Sat · 10:00 AM", "level": "Ages 6–12",
     "desc": "Fun movement games that build coordination and healthy habits."},
]

TRAINERS = [
    {"name": "Jean Claude M.", "role": "Head Coach", "bio": "10 years of strength and conditioning experience.", "initials": "JC"},
    {"name": "Aline U.", "role": "Yoga & Mobility", "bio": "Certified instructor focused on posture and recovery.", "initials": "AU"},
    {"name": "Eric N.", "role": "Boxing Coach", "bio": "Former national amateur boxer who loves teaching beginners.", "initials": "EN"},
    {"name": "Grace K.", "role": "Nutrition Coach", "bio": "Builds realistic meal plans using local Rwandan foods.", "initials": "GK"},
]

PLANS = [
    {"name": "Basic", "price": "25,000", "featured": False,
     "features": ["Gym floor access", "Locker room", "2 group classes / week"]},
    {"name": "Pro", "price": "45,000", "featured": True,
     "features": ["Unlimited gym access", "All group classes", "Monthly body check", "1 free guest pass"]},
    {"name": "Elite", "price": "80,000", "featured": False,
     "features": ["Everything in Pro", "4 personal training sessions", "Nutrition plan", "Priority booking"]},
]


def home(request):
    return render(request, "gym/home.html", {"classes": CLASSES[:3], "plans": PLANS})


def classes(request):
    return render(request, "gym/classes.html", {"classes": CLASSES})


def trainers(request):
    return render(request, "gym/trainers.html", {"trainers": TRAINERS})


def pricing(request):
    return render(request, "gym/pricing.html", {"plans": PLANS})


def contact(request):
    sent = False
    name = ""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        # Later you can save this to a model or send an email.
        sent = True
    return render(request, "gym/contact.html", {"sent": sent, "name": name})