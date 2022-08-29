# ##############################################
# Por posición ####
# ##############################################
def f(x, y, z):
    print(x, y, z)


f(1, 2, 3)
print("", end="\n################\n")

# ##############################################
# Por nombre ####
# ##############################################
def f(x, y, z):
    print(x, y, z)


f(z=3, y=2, x=1)
print("", end="\n################\n")
# ##############################################
# Por mixto - primero de izquierda a derecha  ##
# y luego por nombre ####
# ##############################################
def f(x, y, z):
    print(x, y, z)


f(1, z=3, y=2)
print("", end="\n################\n")
input()