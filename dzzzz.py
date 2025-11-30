import csv


class CarCRUD:
    def __init__(self, filename='cars.csv'):
        self.filename = filename

    def create(self, model, license_plate):
        cars = self.read_all()
        next_id = 1
        if cars:
            next_id = max(int(car['id']) for car in cars) + 1

        with open(self.filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not cars:
                writer.writerow(['id', 'model', 'license_plate'])
            writer.writerow([next_id, model, license_plate])

        print(f"Добавлен: ID {next_id}, {model}, {license_plate}")

    def read_all(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def read_by_id(self, car_id):
        cars = self.read_all()
        for car in cars:
            if car['id'] == str(car_id):
                return car
        return None

    def update(self, car_id, model, license_plate):

        cars = self.read_all()
        found = False

        for car in cars:
            if car['id'] == str(car_id):
                car['model'] = model
                car['license_plate'] = license_plate
                found = True
                break

        if found:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'model', 'license_plate'])
                for car in cars:
                    writer.writerow([car['id'], car['model'], car['license_plate']])
            print(f"Изменен автомобиль ID {car_id}")
        else:
            print("Автомобиль не найден")

    def delete(self, car_id):
        cars = self.read_all()
        new_cars = [car for car in cars if car['id'] != str(car_id)]

        if len(new_cars) < len(cars):
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'model', 'license_plate'])
                for car in new_cars:
                    writer.writerow([car['id'], car['model'], car['license_plate']])
            print(f"Удален автомобиль ID {car_id}")
        else:
            print("Автомобиль не найден")