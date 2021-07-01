# Declare a variable called "city", declare a method that takes city as an argument and value of the city as "London" and method checks if valus is London the true if not false

city = "London"

def check_cityname(city):
    if city.strip().lower() == "london":
        return True
    else:
        return False

print(check_cityname(city))