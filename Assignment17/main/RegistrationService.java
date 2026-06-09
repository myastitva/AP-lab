// =========================
// File: RegistrationService.java
// Location: src/Assignment17/main/
// =========================


public class RegistrationService {

    public boolean registerUser(String email, int age)
            throws InvalidEmailException, UnderageException {

        // Validate email
        if (email == null || email.trim().isEmpty()) {
            throw new InvalidEmailException("Email cannot be null or empty.");
        }

        // Simple email format validation
        if (!email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$")) {
            throw new InvalidEmailException("Invalid email format.");
        }

        // Validate age
        if (age < 18) {
            throw new UnderageException("User must be at least 18 years old.");
        }

        // Registration successful
        return true;
    }
}