from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    item_count = 0  # static/class variable

    def __init__(self, title="Unknown", year=0):
        self.title = title
        self.year = year
        LibraryItem.item_count += 1

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_item_count(cls):
        return cls.item_count


# Subclass: Book
class Book(LibraryItem):
    def __init__(self, title="Unknown", year=0, author="Unknown"):
        super().__init__(title, year)
        self.author = author

    def display_info(self):
        print(f"[Book] Title: {self.title}, Year: {self.year}, Author: {self.author}")

# Subclass: DVD
class DVD(LibraryItem):
    def __init__(self, title="Unknown", year=0, duration=0, genre="Unknown"):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def display_info(self):
        print(f"[DVD] Title: {self.title}, Year: {self.year}, Duration: {self.duration} mins, Genre: {self.genre}")

# User Input Version
def main():
    items = []

    n = int(input("Enter number of items: "))

    for i in range(n):
        print("\n1. Add Book")
        print("2. Add DVD")
        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Enter title: ")
            year = int(input("Enter year: "))
            author = input("Enter author: ")

            items.append(Book(title, year, author))

        elif choice == 2:
            title = input("Enter title: ")
            year = int(input("Enter year: "))
            duration = int(input("Enter duration (mins): "))
            genre = input("Enter genre: ")

            items.append(DVD(title, year, duration, genre))

        else:
            print("Invalid choice!")
            i -= 1

    # Polymorphism
    print("\n--- Library Items ---")
    for item in items:
        item.display_info()

    # Static counter
    print("\nTotal Library Items:", LibraryItem.get_item_count())


if __name__ == "__main__":
    main()