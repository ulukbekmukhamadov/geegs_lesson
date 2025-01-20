class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def  make_computations(self):
        result = self.__cpu * self.__memory  # Простой пример вычислений
        return f'Результат вычислений: {result}'

    def __lt__(self, other):
        return self.cpu < other.cpu

    def __gt__(self, other):
        return self.cpu > other.cpu

    def __eq__(self, other):
        return self.cpu == other.cpu

    def __le__(self, other):
        return self.cpu <= other.cpu

    def __ge__(self, other):
        return self.cpu >= other.cpu

    def __ne__(self, other):
        return self.cpu != other.cpu

    def __str__(self):
        return f'Computer: {self.cpu}, Memory: {self.memory}'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - Beeline'
        elif sim_card_number == 2:
            return f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - O!'

    def __str__(self):
        return f'Phone: {self.sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Phone.__init__(self, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        return f'Маршрут построен до локации: {location}'

    def __str__(self):
        return f'Smart Phone: {self.sim_cards_list}, {self.cpu}/{self.memory}'

acer = Computer(8, 256)
nokia = Phone(['0706458695', '0754554556', '0456874455'])
mi = SmartPhone(8, 512, '0712254452')
samsung = SmartPhone(8, 512, '0712254462')

print(acer)
print(nokia)
print(mi)
print(samsung)

print(mi.use_gps('ak-ordo'))
print(acer.make_computations())
print(nokia.call(1, '0789456123'))
print(acer > mi)
print(mi >= acer)
print(acer < samsung)
print(acer <= samsung)
print(samsung == mi)
print(samsung != mi)
