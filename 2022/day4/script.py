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
        """(FAULTY) - Partially overlapping assignments

        Args:
            another (Assignment): another one to compare to

        Returns:
            Boolean: if they overlap partially (boundaries-inclusive)
        """
        return (self.start <= another.start and self.end >= another.start) or (self.start <= another.end and self.end >= another.end)

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

print(count_full_overlap, count_partial_overlap)