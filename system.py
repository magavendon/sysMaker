class System():
    def __init__(self):
        self.num_of_stars = 1
        self.masses       = [1.00]

    def update_stars(self, stars):
        # Set the new number of stars.
        self.num_of_stars = stars

        # If reducing stars, remove masses.
        while (stars < len(self.masses)):
            self.masses.pop()

        # If adding stars, add masses.
        while (stars > len(self.masses)):
            self.masses.append(0.10)

current = System()
