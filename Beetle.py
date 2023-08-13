"""
Project One:
Beetle

By: Sophia Kist
"""

class Beetle:
    def __init__(self, name):
        self.eyes = 0
        self.antennae = 0
        self.legs = 0
        self.wings = 0
        self.head = False
        self.body = False
        self.name = name

    def handle_num(self, num):
        if num == 6:
            self.body = True
            print("We now have a body")
            return
        if self.body:
            if num == 3 and self.legs < 6:
                self.legs += 1
                print("We now have {} legs".format(self.legs))
                return
            if num == 4 and self.wings < 2:
                self.wings += 1
                print("We now have {} wings".format(self.wings))
                return
            if num == 5:
                self.head = True
                print("We now have a head")
                return
            if self.head:
                if num == 1 and self.eyes < 2:
                    self.eyes += 1
                    print("We now have {} eyes".format(self.eyes))
                    return
                if num == 2 and self.antennae < 2:
                    self.antennae += 1
                    print("We now have {} antennae".format(self.antennae))
                    return

    def is_complete(self):
        return (self.body and self.head and self.eyes == 2 and self.antennae == 2 and self.legs == 6 and self.wings == 2)

def main():
    game = Beetle("Sophia")

    print(game.body)

    game.handle_num(6)
    print(game.body)