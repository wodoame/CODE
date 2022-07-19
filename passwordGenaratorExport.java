
import java.util.Random;
public class Main extends loops {

    public static void main(String[] args) {
        String string_lower;
        String string_upper;
        String numbers;
        String specialCharacters;
        StringBuilder result;
        StringBuilder combination;
        Random getItem = new Random();
        string_lower = "abcdefghijklmnopqrstuvwxyz";
        string_upper = string_lower.toUpperCase();
        numbers = "1234567890";
        specialCharacters = "@&#-_";
        combination = new StringBuilder();
        String[] elements = {string_lower, string_upper, numbers, specialCharacters};
        int n = exceptionInt("\nhow many characters are in the password >> ", "");
        int sample = exceptionInt("how many samples >> ", "");

        for (int do_loop = 0; do_loop < sample; do_loop++) {
            result = new StringBuilder();
            for (String item : elements) {

                int i = getItem.nextInt(0, item.length());
                result.append(item.charAt(i));
                combination.append(item);
            }

            int r = n - 4;
            for (int j = 0; j < r; j++) {

                int i = getItem.nextInt(0, combination.length());
                result.append(combination.charAt(i));
            }

            System.out.printf("\ngenerated password >> %s", result);




        }



       String command = repeat("\n\ndo you want to retry? >> ", "", "y", "n");
        if(command.equals("y")){
            main(null);
        }




    }
}



