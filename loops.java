import java.util.InputMismatchException;
import java.util.Scanner;


public class loops{

    public static int exceptionInt(String message, String messageIfError) {
        Scanner input = new Scanner(System.in);
        int input_val = 0;
        while(true){

            try {
                System.out.print(message);
                input_val = input.nextInt();
            }
            catch(InputMismatchException e){
                System.out.println(messageIfError);
                input.next();
                continue;
            }

            break;

        }

        return input_val;
    }




    public static float exceptionFloat(String message, String messageIfError){
        Scanner input = new Scanner(System.in);
        float input_val = 0;
        while(true){


            try {
                System.out.print(message);
                input_val = input.nextFloat();
            }
            catch(InputMismatchException e){
                System.out.println(messageIfError);
                input.next();
                continue;
            }
            break;

        }

        return input_val;
    }






    public static String loopIfElse(String message, String messageIfError, String... args) {
        Scanner input = new Scanner(System.in);
        boolean contains = false;
        String input_val = "";

        while (!contains) {
            System.out.print(message);
            input_val = input.nextLine().toLowerCase().trim();

            for (String element : args) {
                if (element.equals(input_val)) {
                    contains = true;
                    break;
                }

            }
            if(!contains){
                System.out.println(messageIfError);
            }

        }
        return input_val;
    }


    //end
}


