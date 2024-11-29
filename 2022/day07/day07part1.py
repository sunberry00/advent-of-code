def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()
    
def add_size_to_all_folders(folders, stack, size):
    for index, folder in enumerate(stack):
        abs_path = create_abs_path(stack[:index + 1])
        folders[abs_path] += int(size)
        
def create_abs_path(folders):
    return "/" + str.join("/", folders[1:])
        
    
def part_one():
    input_data = read_input('advent-of-code-24\\2022\\day07\\input.txt')
    current_path = []
    folders = {}
    for line in input_data:
        match line.split():
            case ['$', 'cd', folder]:
                if folder == '..':
                    current_path.pop()
                else:
                    current_path.append(folder)
                    abs_path = create_abs_path(current_path)
                    folders[abs_path] = 0
            case ['$', 'ls']:
                pass
            case ['dir', folder]:
                pass
            case [size, filename]:
                add_size_to_all_folders(folders, current_path, size)
    
    sizes = [size for folder, size in folders.items() if size < 100000]
    print(sum(sizes))
                
    

if __name__ == '__main__':
    part_one()