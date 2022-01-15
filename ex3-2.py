class Tomato:
    states = ["state1", "state2", "state3"] #стадии созревания от посадки до созревания 1-3

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        a = self.states.index(self._state)
        #print("a = ", a, "len = ", len(self.states)-1)
        if a < len(self.states)-1:
            self._state = self.states[a + 1]

    def is_ripe(self):
        return self.states[-1] == self._state


class TomatoBush:
    def __init__(self, amount):
        self.tomatoes = []
        for b in range(amount):
            self.tomatoes.append(Tomato(b))

    def grow_all(self):
        for c in self.tomatoes:
            c.grow()

    def all_are_ripe(self):
        for d in self.tomatoes:
            if not d.is_ripe():
                return False
        return True

    def give_away_all(self):
        self.tomatoes = []
        # for h in self.tomatoes:     ???
        #    del h


class Garderner:
    def __init__(self, name):
        self.name = name
        self._plant = TomatoBush(6) #6 tomatoes

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Ready")
        else:
            print("Not ready")

    @staticmethod
    def knowledge_base():
        print("Knowledge base of...")


Garderner.knowledge_base()
abc = TomatoBush(4)
de = Garderner("Valera")
de.work()
de.harvest()
de.work()
de.harvest()
de.work()
de.harvest()
de.work()
de.harvest()




