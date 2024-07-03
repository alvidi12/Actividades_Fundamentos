Algoritmo numero_mayor
	definir n1, n2, n3, resultado Como Entero;
	escribir "ingresa primer número";
	leer n1;
	escribir "ingresa segundo número";
	leer n2;
	escribir "ingresa tercer número";
	leer n3;
	
	Si n1>n2 y n1>n3 Entonces
		resultado<-n1;
	
	Fin Si
	Si n2>n1 y n2>n3 Entonces
		resultado<-n2;
	
	Fin Si
	Si n3>n2 y n3>n1 Entonces
		resultado<-n3;
	
	Fin Si
	
	Escribir resultado, "= Mayor";
FinAlgoritmo