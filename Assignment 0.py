# -*- coding: utf-8 -*-

h= 0.8 #height of the wall
L= 0.008 #lenght 
w= 1.5 #width of the wall
A= h*w #area of the wall
h_1= 10 #first convective coefficient
h_2= 40 #second convective coeficcient
k= 0.78 #conductive coefficient W/m°C
T_inf1= 20 #temperature of the first convection 
T_inf2= -10 #temperature of the second convection
R_conv1= 1/(h_1*A) #resistance of the first convection
print("The resistance of the first convection is " + str(R_conv1))
R_cond= L/(k*A) #resistance of the conduction
print("The resistance of the conduction is " + str(R_cond))
R_conv2= 1/(h_2*A) #resistance of the second convection
print("The resistance of the second convection is " + str(R_conv2))
R_total= R_conv1+R_cond+R_conv2 #total thermal resistance
Q= (T_inf1-T_inf2)/ R_total     #rate of heat transfer
print("The rate of heat transfer is " + str(Q))
T_1= T_inf1- R_conv1*Q #first inner temperature
print("The questions asked on the problem are : ")
print("The first inner temperature is " + str(T_1))
T_2= T_inf2+ R_conv2*Q #second inner temperature
print("The second inner temperature is " + str(T_2))
Q_cond= (T_1 - T_2)/R_cond #heat transfer of the conduction
print("The heat transfer of the conduction is " + str(Q_cond))




