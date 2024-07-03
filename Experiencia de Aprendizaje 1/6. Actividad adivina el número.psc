Proceso adivina_el_numero
	Definir intentousuario, numeroadivinar, intentos Como Entero;
	Definir acertado Como Logico;
	numeroadivinar <- Aleatorio(1,100);
	acertado <- Falso;
	
	Escribir "solicitud: Ingrese cantidad de intentos";
	Leer intentos;
	
	Mientras intentos>0 Hacer
	Escribir "ingrese un número";
	Leer intentousuario;
	
	si intentousuario = numeroadivinar Entonces
		Escribir "¡FELICITACIONES! , el número ", numeroadivinar, " era el tímido!!";
	acertado <- Verdadero;
	intentos =0;
	SiNo
		intentos = intentos -1;
		Escribir "¡INCORRECTO! , te quedan ", intentos, " intentos más.";
		
	FinSi	
FinMientras
si acertado = Falso Entonces
	Escribir "QUE LÁSTIMA, el número escondido era: ", numeroadivinar;
SiNo
	
FinSi	
FinProceso
