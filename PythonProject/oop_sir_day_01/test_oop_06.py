class Shape:

    def __init__(self, color='', border_width=0):
        self.__color = color
        self.__border_width = border_width

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_border_width(self, border_width):
        self.__border_width = border_width

    def get_border_width(self):
        return self.__border_width

    def __str__(self):
        return self.__color + ' ' + str(self.__border_width)

    def __del__(self):
        print('destroy')


s = Shape('green', 500)
print(s.get_color(), ' ', s.get_border_width())
print(s)
