

def hasil(a):
    return lambda x: x**a  

angka1 = hasil(2) 
print(angka1(15))
#print("Hasil Kuadrat dari angka", angka, "adalah :", hasil )
