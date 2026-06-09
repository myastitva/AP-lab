import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> books = new ArrayList<>();

        // Input 5 book titles
        System.out.println("Enter 5 book titles:");
        for (int i = 1; i <= 5; i++) {
            System.out.print("Book " + i + ": ");
            books.add(sc.nextLine());
        }

        // Search keyword
        System.out.print("\nEnter a word to search: ");
        String keyword = sc.nextLine().toLowerCase();

        // Search books
        boolean found = false;
        System.out.println("\nMatching Books:");

        for (String book : books) {
            if (book.toLowerCase().contains(keyword)) {
                System.out.println(book);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No matching books found.");
        }

        sc.close();
    }
}
