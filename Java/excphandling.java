public class excphandling {
    public static void main(String[] args) {
        try {
            System.out.print("qwerty ");
            int a = 14, b = 2, c;
            c = a / b;
            System.out.print(c);

        } catch (ArithmeticException a) {
            System.out.println("not divisible by zero ");
        } finally {
            System.out.println("qwertykeypad ");
        }
        System.out.println("ended ");
    }

}
