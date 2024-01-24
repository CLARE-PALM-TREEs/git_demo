class thing:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Good day! {self.name}!")
	

earth = thing("world")
earth.greet()

