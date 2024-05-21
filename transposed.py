def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.split())) for line in file]
    return data

def transpose_data(data):
    # 使用zip(*data)進行轉置
    transposed_data = list(map(list, zip(*data)))
    return transposed_data

def write_data(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(' '.join(map(str, line)) + '\n')

# 讀取數據
input_file = 'data.txt'
output_file = 'transposed_data.txt'
data = read_data(input_file)

# 轉置數據
transposed_data = transpose_data(data)

# 寫入轉置後的數據
write_data(output_file, transposed_data)

print(f"轉置後的數據已寫入 {output_file}")
