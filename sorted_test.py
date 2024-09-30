import sorting
import random

# Generate random test data once to ensure all tests use the same input
nums = [random.randint(1, 100) for x in range(random.randint(1, 100))]

def test_bubble():
    assert sorting.bubble(nums.copy()) == sorted(nums), "Bubble sort failed"

def test_selection():
    assert sorting.selection(nums.copy()) == sorted(nums), "Selection sort failed"

def test_insertion():
    assert sorting.insertion(nums.copy()) == sorted(nums), "Insertion sort failed"
