#!/usr/bin/env python


def solve():
    files = {} #{'c.dat': 8504156, 'a/f': 29116}
    folders = set()
    current = []

    with open("day7_input", "r") as f:
        lines = f.readlines()

    for cmd in lines:
        cmd = cmd.strip()
        if cmd.startswith('$'):
            if cmd.startswith('$ cd'):
                folder = cmd[5:]
                if folder == '..':
                    if len(current) > 0:
                        current.pop(-1)
                elif folder == '/':
                    current = []
                else:
                    current.extend(folder.split('/'))
        else: #we have an output from ls
            size, name = cmd.split(' ')
            if size == 'dir':
                continue
            files['/'.join(current + [name])] = int(size) #key is file name with whole path, value is size
        folders.add('/'.join(current)) #collect unique folders

    sum_folder_sizes = 0
    fsizes = {}

    for folder in folders:
        fsize = 0
        for file in files:
            if file.startswith(folder):
                fsize += files[file]
        if fsize <= 100000:
            sum_folder_sizes += fsize
        fsizes[folder] = fsize

    # part 2
    smallest_dir = min(v for v in fsizes.values() if 70000000 - fsizes[""] + v >= 30000000)
 
    return sum_folder_sizes, smallest_dir

def day7():
    results = solve()
    print("Part 1: ", results[0])
    print("Part 2: ", results[1])

day7()