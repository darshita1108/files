class Enemy:
    def __init__(self,x):
        self.energy = x
    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
eva = Enemy(18)

jason.get_energy()
eva.get_energy()