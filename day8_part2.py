with open('input8.txt', 'r') as file:
    puzzle = [line.split(' ') for line in file.read().strip().splitlines()]

def boot(code):
    acc = 0
    i = 0
    ran = set()

    while i not in ran and i != len(code):
        ran.add(i)

        if code[i][0] == 'acc':
            acc += int(code[i][1])
            i += 1
        elif code[i][0] == 'jmp':
            i += int(code[i][1])
        elif code[i][0] == 'nop':
            i += 1
        
    return (i == len(code), acc)

pos = 0

while True:
    at = 0

    for i in range(len(puzzle)):
        if puzzle[i][0] in ('jmp', 'nop'):
            if at == pos:
                puzzle[i] = ('jmp' if puzzle[i][0] == 'nop' else 'nop', puzzle[i][1])
                result = boot(puzzle)

                if result[0]:
                    print(result[1])
                    exit()

                puzzle[i] = ('jmp' if puzzle[i][0] == 'nop' else 'nop', puzzle[i][1])
                break
            
            at += 1
    
    pos += 1