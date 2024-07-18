class Employee:
    def __init__(self) :
        self.cars_sold = 0
        self.revenue_generated = 0.0
        self.position = ""
        self.name = ""

    def set_position(self, positionname):
        self.position = positionname
    
    def get_position(self, position):
        return self.position
    
    def increment_cars_sold(self):
        self.cars_sold += self.cars_sold

    def get_cars_sold(self):
        return self.cars_sold
    
    def get_revenue_generate(self):
        return self.revenue_generated
    
    def generate_revenue(self)
