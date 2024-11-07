import java.util.Scanner;

public class Calculadora {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha uma das opções: +, -, *, / ");
        String operacao = scanner.nextLine();

        System.out.println("Digite o primeiro número: ");
        int primeiroNumero = scanner.nextInt();

        System.out.println(primeiroNumero + " " + operacao);

        System.out.println("Digite o segundo número: ");
        int segundoNumero = scanner.nextInt();

        int resultadoSoma = primeiroNumero + segundoNumero;
        int resultadoSubtracao = primeiroNumero - segundoNumero;
        int resultadoMultiplicacao = primeiroNumero * segundoNumero;
        int resultadoDivisao = primeiroNumero / segundoNumero;

        switch(operacao){

            case "+":
                System.out.println(primeiroNumero + " " + operacao + " " + segundoNumero + " = " + resultadoSoma);
                break;

            case "-":
                System.out.println(primeiroNumero + " " + operacao + " " + segundoNumero + " = " + resultadoSubtracao);
                break;

            case "*":
                System.out.println(primeiroNumero + " " + operacao + " " + segundoNumero + " = " + resultadoMultiplicacao);
                break;

            case "/":
                System.out.println(primeiroNumero + " " + operacao + " " + segundoNumero + " = " + resultadoDivisao);
                break;
        }

        scanner.close();
    }

}
