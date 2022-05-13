cor_preferido = "red"
cor = input("qual é o cor que vc quer? ")
if cor_preferido != cor:
    print("troquei")
    cor_preferido = cor
print("cor preferida: {}".format(cor_preferido))