Algoritmo Muestreo_menor_a_mayor
	Definir n1,n2,n3, resultado Como Entero;
	Escribir "ingrese tres número para el ordenar de menor a mayor";
	leer  n1, n2, n3;
	
	Si n1 > n2 Entonces
		resultado<-n1;
		n1<-n2;
		n2<-resultado;
	Fin Si
	
	Si n2 > n3 Entonces
		resultado<-n2;
		n2<-n3;
		n3<-resultado;
	Fin Si
	Si n1 > n2 Entonces
		resultado<-n1;
		n1<-n2;
		n2<-resultado;
	Fin Si

		Escribir "****Orden menor a mayor****";
	Escribir n1;
	Escribir n2;
	Escribir n3;

FinAlgoritmo
