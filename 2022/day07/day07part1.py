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
    
    total_disk_space = 70_000_000
    required_space = 30_000_000
    used_space = folders['/']
    unused_space = total_disk_space - used_space
    space_to_free = required_space - unused_space
    
    smallest_dir_size = min(
        size for size in folders.values() 
        if size >= space_to_free
    )
    
    print(smallest_dir_size)
    
                
    

if __name__ == '__main__':
    part_one()