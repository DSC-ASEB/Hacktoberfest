import java.util.*;

class CustomExceptionHandling {
    public static void main(String[] args) {
        DrivingLicense d1 = new DrivingLicense("Prateek", 13);

        try {
            d1.createDrivingLicense();
        } catch (UnderAgeException err) {
            System.out.println(err);
        } finally {
            System.out.println("Program Executed Successfully.");
        }
    }
}

class UnderAgeException extends Exception {
    public UnderAgeException(String err) {
        super(err);
    }
}

class DrivingLicense {
    String name;
    int age;

    public DrivingLicense(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void createDrivingLicense() throws UnderAgeException {
        if (this.age < 18) {
            throw new UnderAgeException("You are not old enough to get a driving license");
        }

        else {
            System.out.println("Creating Driving License....");
        }
    }
}