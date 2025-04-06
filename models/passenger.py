class Passenger:
    next_id = 1
    def __init__(self, weight: float):
        """Инициализация пассажира."""
        if weight <=0:
            raise ValueError("Вес пассажира должен быть положительным")
        self.weight = weight
        self.id = Passenger.next_id
        Passenger.next_id += 1
