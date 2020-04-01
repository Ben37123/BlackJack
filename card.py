


class Card(object):


    def __init__(self, name, suit, hardValue, softValue, visible):
        self.__name = name
        self.__suit = suit
        self.__color = ''
        self.__hardValue = hardValue
        self.__softValue = softValue
        self.__visible = visible
        if self.__suit == 'spades' or self.__suit == 'clubs':
            self.__color = 'black'
        else:
            self.__color = 'red'

    def __str__(self):
        if self.__visible == True:
            return(f"""
name = {self.__name}
suit = {self.__suit}
color = {self.__color}
hardValue = {self.__hardValue}
softValue = {self.__softValue}
""")
        else:
            return('Unknown')

    def flip(self):
        self.__visible = True

    def get_name(self):
        return self.__name

    def get_suit(self):
        return self.__suit

    def get_color(self):
        return self.__color

    def get_hardValue(self):
        return self.__hardValue

    def get_softValue(self):
        return self.__softValue

    def get_visible(self):
        return self.__visible

