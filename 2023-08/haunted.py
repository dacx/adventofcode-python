import math


def solve1():
    def navigate_desert(instructions: str, mapping: dict):
        steps: int = 0
        node: str = "AAA"
        while True:  # repeat instr pattern until finished
            for instr in instructions:
                current_node = mapping[node]
                if instr == "L":
                    node = current_node[0]
                else:
                    node = current_node[1]
                steps += 1
                if node == "ZZZ":
                    return steps

    with open("input.txt", "r") as f:
        instructions = f.readline().strip()
        _ = f.readline().strip()  # Skip the second line

        mapping: dict = {}
        for line in f.readlines():
            mapping[line[0:3]] = [line[7:10], line[12:15]]

        print(navigate_desert(instructions, mapping))


def solve2():
    def navigate_as_ghost(instructions: str, mapping: dict, ending_with_a: [str]):
        # after trying to 'brute force' this, i realized that it would take forever.
        # i then looked at the 'cycles' and recognized that they are repetitive
        # so i stored the smallest step count for the cycle in CYCLES and then
        # calculated the lowest common multiple (LCM) of the 6 values. because that's
        # when they are all in sync.
        steps: int = 0
        current_nodes: [str] = ending_with_a
        CYCLES = {}
        while True:  # repeat instr pattern until finished
            for instr in instructions:
                next_up: [str] = []
                for i, node in enumerate(current_nodes):
                    current_node = mapping[node]
                    if instr == "L":
                        node = current_node[0]
                    else:
                        node = current_node[1]
                    next_up.append(node)
                    if node.endswith("Z"):
                        if i not in CYCLES:
                            CYCLES[i] = steps + 1
                    if len(CYCLES) == len(ending_with_a):
                        # https://docs.python.org/3/library/math.html#math.lcm
                        return math.lcm(*CYCLES.values())
                steps += 1
                current_nodes = next_up

    with open("input.txt", "r") as f:
        instructions = f.readline().strip()
        _ = f.readline().strip()  # Skip the second line

        mapping: dict = {}
        ending_with_a: [str] = []

        for line in f.readlines():
            if line[0:3].endswith("A"):
                ending_with_a.append(line[0:3])
            mapping[line[0:3]] = [line[7:10], line[12:15]]

        print(navigate_as_ghost(instructions, mapping, ending_with_a))


if __name__ == "__main__":
    solve1()
    solve2()
