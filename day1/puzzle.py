

def read_input():
    with open("input") as ifile:
        return [int(line) for line in ifile.readlines()]


def cycle(values):
    while True:
        for value in values:
            yield value


def get_frequencies(freq_changes):
    output = 0
    for change in freq_changes:
        yield output 
        output = output + change
    yield output


def get_first_frequency_reached_twice(frequencies):
    visited_frequencies = set()
    for freq in frequencies:
        if freq in visited_frequencies: 
            return freq
        visited_frequencies.add(freq)

print("resulting frequency is : " + str(list(get_frequencies(read_input()))[-1]))
print("first frequency reached twice is: " + str(get_first_frequency_reached_twice(get_frequencies(cycle(read_input())))))
