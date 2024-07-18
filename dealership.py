class Dealership:
    def __init__(self):
        self.staff = []
        self.inventory = []
        self.revenue = 0

    def get_revenue(self):
        return self.revenue
    
    def add_car(self, model_name, used):
        value = 0
        if model_name == "Model1":
            value = 5000
        elif model_name == "Model2":
            value = 10000
        elif model_name == "Model3":
            value = 15000
        else:
            value = 20000

        car = Car(model_name, value, used)

    def get_cars(self):
        return self.inventory