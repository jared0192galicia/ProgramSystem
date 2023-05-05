package tarea;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

public class Tarea2 {

	private static final int ERROR = -1;
	private static final int OR = 1;
	private static final int AND = 2;
	private static final int X = 3;
	private static final int Y = 4;
	private static final int Z = 5;

	private int index = 0;

	private static String cadena = "";
	private static String ret = "";
	private static String lexema = "";

	LinkedList<String> letters = new LinkedList<String>();
	File root = new File("./src/files/file.dmc");	

	Scanner inp = new Scanner(System.in);

	public static void main(String[] args) {
		System.err.println("******* Analizador Lexico *******\n");

		Tarea2 lex = new Tarea2();

		int status;
		boolean casa;
		
		do {
			
			status = lex.estado1();
			casa = true;
			
			switch (status) {
			case ERROR:
				System.err.println("Token erroneo\n  Retorno: " + ret);
				casa = false;
				break;
			case OR:
				System.out.println("Token OR \n  Lexema: or");
				break;
			case AND:
				System.out.println("Token AND \n  Lexema: and");
				break;
			case X:
				System.out.println("Token X \n  Lexema: x");
				break;
			case Y:
				System.out.println("Token Y \n  Lexema: y");
				break;
			case Z:
				System.out.println("Token Z \n  Lexema: z");
				break;

			default:
				throw new IllegalArgumentException("Unexpected value: " + status);
			}
			
			if (!casa) {
				for (String c : lex.letters) {
					if (lex.letters.get(lex.index - 1) == c) {
						System.err.print("__" + c); 
					} else {
						
						System.out.print(c);
					}
				}
				System.out.println();
				break;
			}
		} while (lex.index < lex.letters.size());
		
	}

	public Tarea2() {
		leer();
	}
	
	public void leer() {
		// TODO Auto-generated method stub
		System.out.print("Ingresa la cadena de codigo: ");
		String cadena = inp.nextLine().toLowerCase();


		for (int i = 0; i < cadena.length(); i++) {
			
			if (cadena.charAt(i) != ' ') {
				
				letters.addLast(String.valueOf(cadena.charAt(i)));
			}
		}
		
		System.out.println("Ruta: " + root.toString());
	}

	private int estado1() {
		// TODO Auto-generated method stub

		char c = letters.get(index).charAt(0);
		index++;

		switch (c) {
		case 'o':
			return estado2();
		case 'a':
			return estado4();
		case 'x':
			return estado7();
		case 'y':
			return estado8();
		case 'z':
			return estado9();
		default:
			return estado10();
		}
	}

	private int estado2() {
		// TODO Auto-generated method stub
		char c = letters.get(index).charAt(0);
		index++;

		if (c == 'r') {
			return estado3();
		} else {
			return estado10();
		}

	}

	private int estado3() {
		return OR;
	}

	private int estado4() {
		// TODO Auto-generated method stub
		char c = letters.get(index).charAt(0);
		index++;

		if (c == 'n') {
			return estado5();
		} else {
			return estado10();
		}
	}

	private int estado5() {
		// TODO Auto-generated method stub
		char c = letters.get(index).charAt(0);
		index++;
		
		if (c == 'd') {
			return estado6();
		} else {
			return estado10();
		}
	}

	private int estado6() {
		// TODO Auto-generated method stub
		return AND;
	}

	private int estado7() {
		// TODO Auto-generated method stub
		//char c = letters.get(index).charAt(0);
		
		return X;
	}

	private int estado8() {
		// TODO Auto-generated method stub
//		char c = letters.get(index).charAt(0);

		return Y;
	}

	private int estado9() {
		// TODO Auto-generated method stub
//		char c = letters.get(index).charAt(0);

		return Z;
	}

	private int estado10() {
		return ERROR;
	}
}
