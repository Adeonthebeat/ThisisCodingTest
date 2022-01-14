
# "ULURRDLLU"
# 7
# "LULLLLLLU"
# 7

def solution(dirs):
    answer = 0
    visited = set()
    x, y = 0, 0

    for i in dirs:
        if i == 'L' and x > -5:
            visited.add((( x -1, y), (x, y)))
            x -= 1
        elif i == 'R' and x < 5:
            visited.add(((x, y), ( x +1, y)))
            x += 1
        elif i == 'U' and y < 5:
            visited.add(((x, y), (x, y+ 1)))
            y += 1
        elif i == 'D' and y > -5:
            visited.add(((x, y - 1), (x, y)))
            y -= 1
    answer = len(set(visited))

    print(answer)


if __name__ == "__main__":
    solution("ULURRDLLU")
    solution("LULLLLLLU")
