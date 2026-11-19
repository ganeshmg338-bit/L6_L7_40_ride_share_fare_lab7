
def parse_trip(text):
    if not isinstance(text, str):
        raise ValueError("Trip details must be text")

    parts = text.split(':')
    if len(parts) != 2:
        raise ValueError("Enter cab:distance")

    cab, km = parts

    if not cab.strip():
        raise ValueError("Cab name cannot be empty")

    try:
        distance = float(km)
    except ValueError:
        raise ValueError("Distance must be a number")

    if not math.isfinite(distance) or distance <= 0:
        raise ValueError("Distance must be positive and finite")

    return cab.strip().title(), distance


def fare_average(fares_csv):
    if not isinstance(fares_csv, str) or not fares_csv.strip():
        raise ValueError("Enter valid fares")

    try:
        values = [int(r.strip()) for r in fares_csv.split(',')]
    except ValueError:
        raise ValueError("Fares must be integers")

    if any(value < 0 for value in values):
        raise ValueError("Fares cannot be negative")

    return sum(values) // len(values)


def payable_fare(text):
    if not isinstance(text, str) or text.count('|') != 1:
        raise ValueError("Enter fare|promo")

    fare, promo = text.split('|')

    try:
        fare = float(fare)
        promo = float(promo)
    except ValueError:
        raise ValueError("Fare and promo must be numbers")

    if not math.isfinite(fare) or not math.isfinite(promo):
        raise ValueError("Values must be finite")

    if fare < 0 or promo < 0 or promo > fare:
        raise ValueError("Invalid fare or promo")

    total = fare * 1.18 - promo
    return max(total, 0)


def main():
    print("==== Running parse_trip ====")
    user_input = input("Enter cab:distance in km (e.g. sedan:12): ")
    try:
        print("Cab and Distance:", parse_trip(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running fare_average ====")
    user_input = input("Enter fares as CSV (e.g. 120,95,210): ")
    try:
        print("Average Fare:", fare_average(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running payable_fare ====")
    user_input = input("Enter fare|promo (e.g. 250|30): ")
    try:
        print("Payable Fare:", payable_fare(user_input))
    except ValueError as e:
        print("Invalid input:", e)


import math

if __name__ == "__main__":
    main()
