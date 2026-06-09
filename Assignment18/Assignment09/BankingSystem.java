import java.util.*;
class Account {
    private int accountNumber;
    private String ownerName;
    private double balance;

    public Account() {
        this(0, "Unknown", 0.0);
    }

    public Account(int accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        setBalance(balance);
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance < 0)
            throw new IllegalArgumentException("Invalid Balance");
        this.balance = balance;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        if (ownerName == null || ownerName.isEmpty())
            throw new IllegalArgumentException("Invalid Owner Name");
        this.ownerName = ownerName;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        if (accountNumber <= 0)
            throw new IllegalArgumentException("Invalid Account Number");
        this.accountNumber = accountNumber;
    }

    public void deposit(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Deposit must be positive");
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal must be positive");
        if (amount > balance)
            throw new IllegalArgumentException("Insufficient balance");
        balance -= amount;
    }

    public void display() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Owner Name: " + ownerName);
        System.out.println("Balance: " + balance);
    }
}

// SavingsAccount
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(int accNo, String name, double balance, double interestRate) {
        super(accNo, name, balance);
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        System.out.println("Account Type: Savings Account");
        super.display();
        System.out.println("Interest Rate: " + interestRate);
        System.out.println("Interest Amount: " + calculateInterest());
    }
}

// CurrentAccount
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(int accNo, String name, double balance, double overdraftLimit) {
        super(accNo, name, balance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Invalid amount");

        if (amount > getBalance() + overdraftLimit)
            throw new IllegalArgumentException("Overdraft limit exceeded");

        setBalance(getBalance() - amount);
    }

    @Override
    public void display() {
        System.out.println("Account Type: Current Account");
        super.display();
        System.out.println("Overdraft Limit: " + overdraftLimit);
    }
}

// Main Class
public class BankingSystem {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        List<Account> accounts = new ArrayList<>();

        while (true) {
            System.out.println("\n1. Add Savings Account");
            System.out.println("2. Add Current Account");
            System.out.println("3. Display All Accounts");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");

            int choice = sc.nextInt();

            try {
                switch (choice) {
                    case 1:
                        System.out.print("Enter Account Number: ");
                        int sAccNo = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter Owner Name: ");
                        String sName = sc.nextLine();

                        System.out.print("Enter Balance: ");
                        double sBal = sc.nextDouble();

                        System.out.print("Enter Interest Rate: ");
                        double rate = sc.nextDouble();

                        accounts.add(new SavingsAccount(sAccNo, sName, sBal, rate));
                        System.out.println("Savings Account Added!");
                        break;

                    case 2:
                        System.out.print("Enter Account Number: ");
                        int cAccNo = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter Owner Name: ");
                        String cName = sc.nextLine();

                        System.out.print("Enter Balance: ");
                        double cBal = sc.nextDouble();

                        System.out.print("Enter Overdraft Limit: ");
                        double limit = sc.nextDouble();

                        accounts.add(new CurrentAccount(cAccNo, cName, cBal, limit));
                        System.out.println("Current Account Added!");
                        break;

                    case 3:
                        if (accounts.isEmpty()) {
                            System.out.println("No accounts to display.");
                        } else {
                            for (Account acc : accounts) {
                                System.out.println("\n--- Account Details ---");
                                acc.display();
                            }
                        }
                        break;

                    case 4:
                        System.out.println("Exiting...");
                        sc.close();
                        return;

                    default:
                        System.out.println("Invalid choice!");
                }
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                sc.nextLine();
            }
        }
    }
}
