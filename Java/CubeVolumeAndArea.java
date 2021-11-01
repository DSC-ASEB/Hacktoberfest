import java.util.Scanner;

public class CubeVolumeAndArea {
    public static void main(String[] args) {
        double volume, side, surfaceArea;
        Scanner scan;
        scan = new Scanner(System.in);
        System.out.println("Enter length of cube side");
        side = scan.nextDouble();
        surfaceArea = 6 * side * side; //Total surface area
        volume = side * side * side;
        System.out.format("Surface Area = %.3f \n", surfaceArea);
        System.out.format("Volume = %.3f \n", volume);
    }
}
