
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class RegistrationServiceTest {

    private RegistrationService registrationService;

    @BeforeEach
    void setUp() {
        registrationService = new RegistrationService();
    }

    @Test
    void testSuccessfulRegistration() throws InvalidEmailException, UnderageException {
        assertTrue(
                registrationService.registerUser("user@example.com", 25)
        );
    }

    @Test
    void testNullEmailThrowsInvalidEmailException() {
        assertThrows(
                InvalidEmailException.class,
                () -> registrationService.registerUser(null, 25)
        );
    }

    @Test
    void testInvalidEmailFormatThrowsInvalidEmailException() {
        assertThrows(
                InvalidEmailException.class,
                () -> registrationService.registerUser("invalid-email", 25)
        );
    }

    @Test
    void testUnderageThrowsUnderageException() {
        assertThrows(
                UnderageException.class,
                () -> registrationService.registerUser("user@example.com", 16)
        );
    }

    @Test
    void testEmptyEmailThrowsInvalidEmailException() {
        assertThrows(
                InvalidEmailException.class,
                () -> registrationService.registerUser("", 25)
        );
    }
}