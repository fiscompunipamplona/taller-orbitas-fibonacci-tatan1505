#Haga un pograma que calcule la velocidad y la posición en el afelio, siempre dando los valores de la posición y velocidad en el perihelio
from math import pi
Xp=float(input("\n Ingrese la posición en el perihelio en metro\n"))
Vp=float(input("\n Ingrese la velocidad en el perihelio en metro\n "))
M_e=1.989e30 #La masa de la estrella de neutrones 
#Hallamos la posición o la velocidad en el afelio entonces partimos de las siguientes ecuaciónes
G=6.674e-11
a=1
b=(2*G*M_e)/(Xp*Vp)
c=((Vp**2)-((2*G*M_e)/Xp))
j=((b**2)-(4*a*c))**(1/2)
V1=((-b+j)/(2*a))
V2=((-b-j)/(2*a))
print("la 1 velocidad en el afelio es",V1*(1e-4))
print("la 2 velocidad en el afelio es",V2*(1e-4))

    #Entonces hallamos a la posición en el afelio partiendo de la segunda ley de Kepler para la primera velocidad
print("para la velocidad 1 ")
h=Xp*Vp
Xa=h/V1
print(" el valor de la posición en el  afelio es:",Xa*(1e-4))
semi_may=(1/2)*(Xp+Xa)
semi_me=(Xa*Xp)**(1/2)
T=(2*pi*semi_may*semi_me)/(Xp*Vp)
e=(Xa-Xp)/(Xa+Xp)
print("\n el valor del semieje mayor en metro es ",semi_may*(1e-5))
print("\n el valor del semieje menor en metro es",semi_me*(1e-5))
print("\n el valor del periodo en segundo es",T*(1e-3))
print("\n el valor de la excentricidad es",e*(1e-2))
#Ahora la hallamos la posición para la segunda velocidad
print("para la 2 velocidad ")
Xa=((Xp*Vp)/V2)
print(" el valor de la posición en el  afelio es:",Xa*(1e-4))
semi_may=(1/2)*(Xp+Xa)
semi_me=(Xa*Xp)**(1/2)
T=(2*pi*semi_may*semi_me)/(Xp*Vp)
e=(Xa-Xp)/(Xa+Xp)
print("\n el valor del semieje mayor en metro es ",semi_may*(1e-5))
print("\n el valor del periodo en segundo es",T*(1e-3))
print("\n el valor de la excentricidad es",e*(1e-2))

    
    
    
    
    
        

            
