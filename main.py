import csv


def main():
    while True:
        print("\nGYM! Equipment Finder")
        print("1. Search by equipment")
        print("2. Show all gyms")
        print("3. Show all equipment ")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            equipment_input = input("What equipment are you looking for? Separate multiple machines with commas: ")
            equipment_list = [
                machine.strip()
                for machine in equipment_input.split(",")
                if machine.strip()
            ]

            if not equipment_list:
                print("\nPlease enter at least one piece of equipment.")
                continue
            
            gyms = search_equipment(equipment_list)

            if len(gyms) == 0:
                print("No gyms found.")
            else:
                print(f"\nGyms with {', '.join(equipment_list)}:")

                for gym in gyms:
                    address = get_address(gym)
                    print(f"{gym} - {address}")

        elif choice == "2":
            show_all_gyms()

        elif choice == "3":
            show_all_equipment()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


def search_equipment(requested_equipment):
    matches = []

    with open("equipment.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            gym_equipment = row["equipment"].split(";")

            gym_equipment = [
                machine.strip().lower()
                for machine in gym_equipment
            ]

            all_found = True

            for requested_machine in requested_equipment:
                requested_machine = requested_machine.strip().lower()

                found = False

                for machine in gym_equipment:
                    if requested_machine in machine:
                        found = True
                        break

                if found == False:
                    all_found = False
                    break

            if all_found:
                matches.append(row["gym"])

    return matches


def get_address(gym_name):
    with open("gyms.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["gym"] == gym_name:
                return row["address"]

    return "Address not found"


def show_all_gyms():
    print("\nAll gyms:")

    with open("gyms.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f'{row["gym"]} - {row["address"]}')


def show_all_equipment():
    equipment_set = set()

    with open("equipment.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            equipment_list = row["equipment"].split(";")

            for machine in equipment_list:
                equipment_set.add(machine.strip())

    print("\nAvailable equipment:")

    for machine in sorted(equipment_set):
        print(machine)


if __name__ == "__main__":
    main()