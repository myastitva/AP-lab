#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define INCREMENTS 1000000

long long counter = 0;
pthread_mutex_t mutex;

void *increment_without_mutex(void *arg) {
    for (int i = 0; i < INCREMENTS; i++) {
        counter++;
    }
    return NULL;
}

void *increment_with_mutex(void *arg) {
    for (int i = 0; i < INCREMENTS; i++) {
        pthread_mutex_lock(&mutex);
        counter++;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];

    /* Without synchronization */
    counter = 0;

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL,
                       increment_without_mutex, NULL);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Without mutex: %lld (Expected: %lld)\n",
           counter,
           (long long)NUM_THREADS * INCREMENTS);

    /* With mutex */
    counter = 0;
    pthread_mutex_init(&mutex, NULL);

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL,
                       increment_with_mutex, NULL);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("With mutex: %lld (Expected: %lld)\n",
           counter,
           (long long)NUM_THREADS * INCREMENTS);

    pthread_mutex_destroy(&mutex);

    return 0;
}