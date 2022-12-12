with open('./input.txt', 'r') as f:
    lines = f.readlines()


class Assignment:
    def __init__(self, range) -> None:
        [self.start, self.end] = [int(_) for _ in range.split('-')]
    
    def fully_overlaps(self, another: 'Assignment'):
        """Fully-overlapping assignments

        Args:
            another (Assignment): another one to compare to

        Returns:
            Boolean: if they overlap fully (boundaries-inclusive)
        """
        return (self.start <= another.start and self.end >= another.end) or (another.start <= self.start and another.end >= self.end)

    def partially_overlaps(self, another: 'Assignment'):
        """Partially overlapping assignments

        Args:
            another (Assignment): another one to compare to

        Returns:
            Boolean: if they overlap partially (boundaries-inclusive)
        """
        return self.fully_overlaps(another) or (Assignment._is_between(self.start, self.end, another.start)) or (Assignment._is_between(another.start, another.end, self.start))

    @staticmethod
    def _is_between(min: int, max: int, value: int):
        return value >= min and value <= max

count_full_overlap = 0
count_partial_overlap = 0

for line in lines:
    line = line.strip('\n')

    if not line:
        break

    [x, y] = line.split(',')
    first = Assignment(x)
    second = Assignment(y)

    # Part 1
    if first.fully_overlaps(second):
        count_full_overlap += 1
    
    # Part 2
    if first.partially_overlaps(second):
        count_partial_overlap += 1

print(f'{count_partial_overlap} assignments overlap, among them {count_full_overlap} are fully overlapping.')