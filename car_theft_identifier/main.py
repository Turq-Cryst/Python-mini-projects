class Car:
    def __init__(self, licence_plate: str) -> None:
        if len(licence_plate) != 6:
            raise ValueError('Invalid license plate.')

        self.licence_plate = licence_plate


class StolenCarRegistry:
    def __init__(self) -> None:
        self.stolen_plates: set[str] = set()

    def add_stolen_plates(self, plates: list[str]) -> None:
        for plate in plates:
            self.stolen_plates.add(plate.upper())

    def remove_stolen_plate(self, plate: str) -> None:
        plate = plate.upper()
        if plate in self.stolen_plates:
            self.stolen_plates.remove(plate)
            print(f'Successfully removed {plate} from Registry.')
        else:
            print(f'{plate} not registered as stolen.')

    def is_stolen(self, plate: str) -> bool:
        return plate.upper() in self.stolen_plates

    def disp_stolen_plates(self) -> None:
        for plate in self.stolen_plates:
            print(f'{plate}', end='\n')


def main() -> None:
    registry: StolenCarRegistry = StolenCarRegistry()

    registry.add_stolen_plates(['ABC123', 'ZYX321', 'TIM740'])

    print('---Welcome to Car Theft Identifier---')
    print('1. Check if car is stolen')
    print('2. Show all stolen cars')
    print('3. Remove a car from registry')
    print('4. Exit program')

    while True:
        try:
            user_input: int = int(input('Enter an option: '))
        except ValueError:
            print('Enter a number, for e.g., 2')
            continue


        if user_input == 1:
            plate: str = input('Enter car licence plate: ').strip()
            car: Car = Car(plate)
            if registry.is_stolen(car.licence_plate):
                print(f'❌ Car with plate "{car.licence_plate}" is: REPORTED STOLEN!')
            else:
                print(f'✅ Car with plate "{car.licence_plate}" is: OK')
        elif user_input == 2:
            registry.disp_stolen_plates()
        elif user_input == 3:
            plate: str = input('Enter the licence plate no.: ').strip()
            car: Car = Car(plate)
            registry.remove_stolen_plate(car.licence_plate)
        elif user_input == 4:
            print('Exiting...')
            break
        else:
            print('Invalid input.')



if __name__ == '__main__':
    main()

