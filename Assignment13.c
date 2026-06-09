#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;        // Character buffer
    size_t length;     // Number of characters currently stored
    size_t capacity;   // Total allocated size (including null terminator space)
} StringBuffer;

/*
 * Allocate and initialize a new StringBuffer.
 * Returns NULL if memory allocation fails.
 */
StringBuffer *sb_init(size_t initial_capacity) {
    if (initial_capacity == 0) {
        initial_capacity = 1;  // Ensure at least one byte is allocated
    }

    StringBuffer *sb = malloc(sizeof(StringBuffer));
    if (sb == NULL) {
        fprintf(stderr, "malloc failed for StringBuffer\n");
        return NULL;
    }

    sb->data = malloc(initial_capacity);
    if (sb->data == NULL) {
        fprintf(stderr, "malloc failed for data buffer\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;
    sb->data[0] = '\0';

    return sb;
}

/*
 * Append a C string to the StringBuffer.
 * Automatically doubles capacity until enough space exists.
 * Returns 0 on success, -1 on allocation failure.
 */
int sb_append(StringBuffer *sb, const char *str) {
    if (sb == NULL || str == NULL) {
        return -1;
    }

    size_t str_len = strlen(str);
    size_t required = sb->length + str_len + 1; // +1 for '\0'

    /* Grow the buffer until it is large enough */
    if (required > sb->capacity) {
        size_t new_capacity = sb->capacity;

        while (new_capacity < required) {
            new_capacity *= 2;
        }

        /* Safe realloc: use a temporary pointer */
        char *temp = realloc(sb->data, new_capacity);
        if (temp == NULL) {
            fprintf(stderr, "realloc failed\n");
            return -1;
        }

        sb->data = temp;
        sb->capacity = new_capacity;

        printf("Buffer grew to capacity: %zu\n", sb->capacity);
    }

    /* Append the new string */
    memcpy(sb->data + sb->length, str, str_len + 1); // Copy including '\0'
    sb->length += str_len;

    return 0;
}

/*
 * Free both the internal data buffer and the StringBuffer itself.
 */
void sb_free(StringBuffer *sb) {
    if (sb != NULL) {
        free(sb->data);
        free(sb);
    }
}

int main(void) {
    /* Start small so growth happens multiple times */
    StringBuffer *sb = sb_init(8);
    if (sb == NULL) {
        return 1;
    }

    printf("Initial capacity: %zu\n", sb->capacity);

    /* These appends will force the buffer to grow several times */
    if (sb_append(sb, "Hello") != 0) {
        sb_free(sb);
        return 1;
    }

    if (sb_append(sb, ", Dynamic") != 0) {
        sb_free(sb);
        return 1;
    }

    if (sb_append(sb, " String Buffer Example!") != 0) {
        sb_free(sb);
        return 1;
    }

    printf("\nFinal string: %s\n", sb->data);
    printf("Length: %zu\n", sb->length);
    printf("Final capacity: %zu\n", sb->capacity);

    /* Destructor: release all allocated memory */
    sb_free(sb);

    return 0;
}