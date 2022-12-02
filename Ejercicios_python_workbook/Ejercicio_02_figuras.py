def figura_lados(num):
    figuras = {
        3:"triangulo",
        4:"cuadrado",
        5:"pentágono",
        6:"hexágono",
        7:"heptágono",
        8:"octágono",
        9:"eneágono",
        10:"decágono"}
        
    valor = figuras.get(num)
    return valor


print(figura_lados(10))