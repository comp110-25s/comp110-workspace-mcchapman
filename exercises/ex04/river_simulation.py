from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear
from exercises.ex04.river import River

my_river = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.check_ages()
my_river.one_river_week

print(f"Fish population before removing: {len(my_river.fish)}")
print(f"Bear population before removing: {len(my_river.bears)}")
my_river.remove_fish(amount=3)
print(f"Fish population after removing 3: {len(my_river.fish)}")
print(f"Bear population after check ages: {len(my_river.bears)}")
