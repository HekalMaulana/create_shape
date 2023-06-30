from turtle import Turtle,Screen
from random import choice

my_t = Turtle()
screen = Screen()

colours = ['red', 'green', 'blue', 'yellow', 'pink']

def draw_shape(side): # Membuat sebuah function untuk membentuk sebuah sudut
    angle = 360 / side #menentukan sudut yang akan dibuat. Contoh : 360 / 3 = 120, maka sudut yang akan dibuat adalah segitiga
    for _ in range(side): # mengulang program sebanyak berapa sudut yang akan dibuat. Contoh apabila sidee = 3 maka jumlah perulangan sebanyak 3 kali
        my_t.forward(100)
        my_t.right(angle)


for _ in range(3, 11): # membuat perulangan untuk mendapatkan nilai berapa banyak jumlah sudut yang akan dibuat
    my_t.color(choice(colours)) # mendapatkan random color dari random module
    draw_shape(_) # memamnggil function draw_shape dan mengisi parameternya dengan jumlah sudut (didapat dari perulangan yang mendapatkan nilai jumlah sudut)


screen.exitonclick() # sebuah method di class Screen yang ada di turlte module. Berguna untuk menutup layar ketika di click