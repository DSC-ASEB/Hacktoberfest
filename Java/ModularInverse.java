import java.util.Scanner;

public class ModularInverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = 1;

        //Input
        //multiplicate inverse of 'a' under modulo 'm'
        //Enter value's of 'a' and 'm'
        System.out.println("Enter value of 'a'");
        int a = sc.nextInt();
        System.out.println("Enter value of 'm");
        int m = sc.nextInt();

        int values[] = extendedEuclidean(a, m);
        int gcd = values[0];
        if (gcd != 1)
            System.out.println("Solution doesn't exists");
        else {
            x = values[1];
            x = (x % m + m) % m;
            System.out.println("Multiplicative Inverse 'a' modulo 'm' is " + x);
        }
        sc.close();
    }


    public static int[] extendedEuclidean(int a, int m)
    {
        // Base Case
        if (m == 0) {
            return new int[] {a, 1, 0};
        }
        
        int vals[] =  extendedEuclidean(m, a % m);
        int gcd = vals[0];
        int x = vals[2];
        int y = vals[1] - (a / m) * x;
        return new int[] {gcd, x, y};
    }
}