class thing:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi {self.name}!")
	

earth = thing("world")
earth.greet()

