# This update was made in the random-numbers branch
# Added a simple example of random target generation
import random

example_array = sorted(random.sample(range(1, 100), 10))
example_target = random.choice(example_array)
print("Example array:", example_array)
print("Random target for testing:", example_target)

