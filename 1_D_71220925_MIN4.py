print("BARISAN ARITMATIKA")
a = int(input("masukkan bilangan awal:"))
b = int(input("masukkan selisih bilangan:"))
n = int(input("masukkan banyaknya bilangan :"))
n1= n-1

def total (a,b,n1):
    return (n*0.5)*2*a + n1*b
 
print("Total dari deret aritmatika tersebut adalah:", total)