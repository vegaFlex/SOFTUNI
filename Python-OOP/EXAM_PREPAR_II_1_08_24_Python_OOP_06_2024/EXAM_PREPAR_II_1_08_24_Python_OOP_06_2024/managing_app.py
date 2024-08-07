from EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.user import User
from EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.vehicles.passenger_car import PassengerCar
from EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.vehicles.cargo_van import CargoVan
from EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.route import Route


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if any(user.driving_license_number == driving_license_number for user in self.users):
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ['PassengerCar', 'CargoVan']:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if any(vehicle.license_plate_number == license_plate_number for vehicle in self.vehicles):
            return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == 'PassengerCar':
            vehicle = PassengerCar(brand, model, license_plate_number)
        elif vehicle_type == 'CargoVan':
            vehicle = CargoVan(brand, model, license_plate_number)

        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next((user for user in self.users if user.driving_license_number == driving_license_number), None)
        vehicle = next((vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number),
                       None)
        route = next((route for route in self.routes if route.route_id == route_id), None)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        status = "OK" if not vehicle.is_damaged else "Damaged"
        return f"{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} Battery: {vehicle.battery_level}% Status: {status}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([v for v in self.vehicles if v.is_damaged], key=lambda v: (v.brand, v.model))
        repaired_count = 0

        for vehicle in damaged_vehicles[:count]:
            vehicle.change_status()
            vehicle.recharge()
            repaired_count += 1

        return f"{repaired_count} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        report = "*** E-Drive-Rent ***\n"
        report += "\n".join(str(user) for user in sorted_users)
        return report
