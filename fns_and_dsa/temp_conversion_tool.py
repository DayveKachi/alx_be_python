FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    answer = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return answer


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    answer = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return answer


def main():
    temperature = input("Enter the temperature to convert: ")
    if temperature.isnumeric():
        temperature = float(temperature)
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        temp_type_options = ["C", "F"]
        if temp_type.isalpha() and temp_type.upper() in temp_type_options:
            match temp_type.upper():
                case "C":
                    result = convert_to_fahrenheit(temperature)
                    print(
                        f"{temperature}",
                        chr(176),
                        "C is ",
                        f"{result}",
                        chr(176),
                        "F",
                        sep="",
                    )
                case "F":
                    result = convert_to_celsius(temperature)
                    print(
                        f"{temperature}",
                        chr(176),
                        "F is ",
                        f"{result}",
                        chr(176),
                        "C",
                        sep="",
                    )
        else:
            print("Invalid temperature type. Please enter C/F.")
    else:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
