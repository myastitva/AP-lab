import sys
import gc
gc.enable()

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    def __repr__(self):
        return f"Node({self.name})"

A = Node("A")
B = Node("B")

A.link = B
B.link = A

print("Created cycle:")
print("A ->", A.link)
print("B ->", B.link)

# Check reference counts

print("\nReference counts (includes temporary reference):")
print("A:", sys.getrefcount(A))
print("B:", sys.getrefcount(B))

# the object IDs so we can investigate after deletion
a_id = id(A)
b_id = id(B)

gc.disable()

del A
del B

print("\nDeleted variables A and B.")


print("\nObjects still tracked by the garbage collector:")
found = []
for obj in gc.get_objects():
    if id(obj) in (a_id, b_id):
        found.append(obj)
        print("Still alive:", obj)

print(f"Found {len(found)} cyclic objects still in memory.")
collected = gc.collect()

print(f"\nGarbage collector found and collected {collected} unreachable objects.")

# Verify they are gone
print("\nChecking if objects still exist after gc.collect():")
still_exists = any(id(obj) in (a_id, b_id) for obj in gc.get_objects())
print("Objects still tracked?", still_exists)

gc.enable()
