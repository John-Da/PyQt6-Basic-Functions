class WeatherStation:
    def __init__(self, location, temperature):
        self.__location = location
        self.__temperature = temperature

    
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    def get_location(self):
        return self.__location
    
    def set_location(self, new_location):
        self.__location = new_location

    def get_temperature(self):
        





station1 = WeatherStation("New York", 22.5)
station2 = WeatherStation("Los Angeles", 28.5)

print(station1)
print(station2)

print(f"35˚C is {WeatherStation.celsius_to_fahrenheit(35):.1f}˚F")