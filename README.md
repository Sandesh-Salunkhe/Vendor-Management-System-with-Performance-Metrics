# Vendor-Management-System-with-Performance-Metrics (Work in Progress)
# Objective : 
  Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

# Project Status:
🚧 Work in Progress 🚧

As of now, I'm actively engaged in crafting and refining this system. Expect continuous updates and enhancements to bring about a feature-rich and reliable Vendor Management Solution.

Feel free to explore the code and contribute ideas or improvements. Your feedback is highly appreciated! Let's build something great together. 🚀


#### Step 1:
python manage.py makemigrations
#### Step 2: 
python manage.py migrate
#### Step 3: 
python manage.py shell

#### Run the following command/code 
from Metrics.models import SubscriptionPlan
initial_data = [
    {"name": "Free Plan", "duration_months": 1, "price": 0},
    {"name": "Basic Plan", "duration_months": 6, "price": 499},
    {"name": "Pro Plan", "duration_months": 12, "price": 899},
    {"name": "Enterprise Plan", "duration_months": 20, "price": 1799},
]

for data in initial_data:
    SubscriptionPlan.objects.create(**data)
