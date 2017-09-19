class AudioVisual:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
    def switch(self, on_off):
        self.power = on_off
    def set_volume(self, vol):
        self.volume = vol
class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)
    def tune(self):
        str = 'la la la...' if self.power else "turn it on"
        print(str)
class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size
    def watch(self):
        str = "have fan!" if self.power else "switch on"
        print(str)
aud = Audio(False, 37)
print(aud.power)
print(aud.volume)
aud.tune()
aud.switch(True)
aud.tune()
tv = TV(False, 27, 100)
print(tv.power)
print(tv.volume)
print(tv.size)
tv.watch()
tv.switch(True)
tv.watch()

# class TV:
#     def __init__(self, power, volume, size):
#         self.power = power
#         self.volume = volume
#         self.size = size
#     def switch(self, on_off):
#         self.power = on_off
#     def set_volume(self, vol):
#         self.volume = vol
#     def watch(self):
#         str = "have fan!" if self.power else "switch on"
#         print(str)
# tv = TV(False, 37, 100)
# tv.switch(True)
# tv.watch()


# class Audio:
#     def __init__(self, power, volume):
#         self.power = power
#         self.volume = volume
#     def switch(self, on_off):
#         self.power = on_off
#     def set_volume(self, volume):
#         self.volume = volume
#     def tune(self):
#         str = "la la la....." if self.power else "turn it on"
#         print(str)
# mp3 = Audio(False, 37)
# print(mp3.power)
# print(mp3.volume)
# mp3.set_volume(27)
# print(mp3.volume)
# mp3.tune()
# mp3.switch(True)
# mp3.tune()

# import pygame
# class MyRect(pygame.Rect):
#     def flip(self):
#         self.width, self.height = (self.height, self.width)
# r = MyRect(10, 20, 30, 40)
# print(r.size)
# r.flip()
# print(r.size)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         print("Hi! " + self.name)
# he = Person("tanaka")
# she = Person("yamada")
# print(he.name)
# print(she.name)
# he.say_hello()

# class Pen:
#     def __init__(self, length, color):
#         self.length = length
#         self.color = color
#     def write(self, how_many_hours):
#         self.length -= how_many_hours / 10
# pen1 = Pen(5, "red")
# pen2 = Pen(10, "black")
# print(pen1.length)
# # print(pen2.color)
# pen1.write(7)
# print(pen1.length)
