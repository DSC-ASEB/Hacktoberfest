import java.util.Scanner;

//Easily find volume and surface area of cubes
public class CubeVolumeAndArea {

    public static void main(String[] args) {
        double volume, side, surfaceArea;
        Scanner scan;
        scan = new Scanner(System.in);

        System.out.println("Enter Length of cube side");
        side = scan.nextDouble();

        //Total surface area
        surfaceArea = 6 * side * side;

        //Cube Volume
        volume = side * side * side;

        // Outputs
        System.out.format("Surface Area = %.3f \n", surfaceArea);
        System.out.format("Volume = %.3f \n", volume);

    }
}