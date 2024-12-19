'''
Advent Of Code 2024! Day 1
Shout out to my friend Eric Wastl (github.com/topaz)! So proud of how far you've taken Advent of Code and the excitement this
brings all of us!
'''

def main():

    left = []
    right = []

    with open('day1_input.txt', 'r') as file:
        for line in file:
            input_line = line.strip().split()
            left.append(int(input_line[0]))
            right.append(int(input_line[1]))

    left.sort()
    right.sort()

    print("Part 1 Answer: " + str(part1(left,right)))
    print("Part 2 Answer: " + str(part2(left,right)))

def part1(left,right):

    i = 0
    distance = 0

    while i < len(left):
        distance += abs(left[i] - right[i])
        i += 1

    return distance

def part2(left, right):

    sim_score = 0

    for left_item in left:

        dup_count = 0

        for right_item in right:
            if left_item == right_item:
                dup_count += 1

        sim_score += left_item * dup_count

    return sim_score

if __name__ == '__main__':
    main()