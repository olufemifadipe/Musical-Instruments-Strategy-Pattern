
"""
COP4814 - Component-Based Software Development
Lab #1 - Implementing the Strategy Design Pattern
for Musical Instruments

Author: Olufemi Rafael Fadipe
"""

from abc import ABC, abstractmethod


###############################################################################
# Instruments
###############################################################################

class Instrument(ABC):
    play_behavior = None

    @abstractmethod
    def display(self):
        pass

    def set_play_behavior(self, play_behavior):
        self.play_behavior = play_behavior

    def perform_play(self):
        self.play_behavior.play()


class DoubleBass(Instrument):

    def __init__(self):
        self.play_behavior = PlayWithBow()

    def display(self):
        print("I am a double bass.")


class Clarinet(Instrument):

    def __init__(self):
        self.play_behavior = BuzzAReed()

    def display(self):
        print("I am a clarinet.")


class Harp(Instrument):

    def __init__(self):
        self.play_behavior = PluckWithFingers()

    def display(self):
        print("I am a harp.")


class Tuba(Instrument):

    def __init__(self):
        self.play_behavior = BuzzWithLips()

    def display(self):
        print("I am a tuba.")


class Violin(Instrument):

    def __init__(self):
        self.play_behavior = PlayWithBow()

    def display(self):
        print("I am a violin.")


###############################################################################
# Play Behaviors
###############################################################################

class PlayBehavior(ABC):

    @abstractmethod
    def play(self):
        pass


class PlayWithBow(PlayBehavior):

    def play(self):
        print("Playing the instrument with a bow.")


class BuzzAReed(PlayBehavior):

    def play(self):
        print("Playing the instrument by buzzing a reed.")


class PluckWithFingers(PlayBehavior):

    def play(self):
        print("Playing the instrument by plucking strings.")


class BuzzWithLips(PlayBehavior):

    def play(self):
        print("Playing the instrument by buzzing lips.")


###############################################################################
# Main Program
###############################################################################

def main():

    instruments = [
        DoubleBass(),
        Clarinet(),
        Harp(),
        Tuba(),
        Violin()
    ]

    for instrument in instruments:
        instrument.display()
        instrument.perform_play()
        print()

    # Demonstrating a change in playing behavior
    print("Changing the violin's playing behavior:")

    violin = Violin()
    violin.set_play_behavior(PluckWithFingers())

    violin.display()
    violin.perform_play()


if __name__ == "__main__":
    main()
