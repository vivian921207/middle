import ast

def ben_encrypt(msg, pad):
    """Encrypts message `msg' using Ben's One-time-pad with feedback algorithm"""
    assert len(msg) == len(pad)
    prev_c = 0
    result = []
    for i in range(len(msg)):
        c = msg[i] ^ ((pad[i] + prev_c) % 256)
        result.append(c)
        prev_c = c
    return result

def ben_decrypt_single_byte(c, p, prev_c):
    """Decrypts a single byte using Ben's One-time-pad with feedback algorithm"""
    return c ^ ((p + prev_c) % 256)

def text_to_bytes(t):
    return [ord(c) for c in t]

# 檢查是否為有效英文文本符號（包括字母、空格和一些標點符號）
def is_valid_character(char):
    return (65 <= char <= 90) or (97 <= char <= 122) or char in (32, 33, 44, 46, 63, 39 ,40,41,45)

# 找到使所有ci均為有效英文文本符號的所有可能的p
def find_all_valid_p(c_list, prev_c_list):
    valid_p_list = []
    for p in range(256):  # 遍歷所有可能的p值
        if all(is_valid_character(ben_decrypt_single_byte(c, p, prev_c)) for c, prev_c in zip(c_list, prev_c_list)):
            valid_p_list.append(p)
    return valid_p_list  # 返回所有可能的p值

# 讀取文件中的數據
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [ast.literal_eval(line.strip()) for line in file]
    return data

# 寫入解密結果到文件
def write_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        for result in results:
            for line in result:
                file.write(''.join(line) + '\n')
            file.write('\n')

# 統計所有可能的60輪解密結果
def decrypt_all_possible_results(input_file):
    data = read_data(input_file)
    prev_c_list = [0] * len(data[0])  # 初始值c'為0
    all_decoded_matrices = []  # 存儲所有解密矩陣

    for i in range(len(data)):
        c_list = data[i]
        valid_p_list = find_all_valid_p(c_list, prev_c_list)

        if valid_p_list:
            print(f"第{i + 1}輪次找到的有效密鑰p列表: {valid_p_list}")
            for p in valid_p_list:
                # 創建新的解碼矩陣
                decoded_matrix = [[] for _ in range(len(data[0]))]
                decrypted_message = [
                    chr(ben_decrypt_single_byte(c, p, prev_c)) for c, prev_c in zip(c_list, prev_c_list)
                ]
                print(f"使用密鑰p = {p}解密後的消息: {''.join(decrypted_message)}")
                # 將每一個解密結果添加到解碼矩陣的對應行
                if (i == 0 and p == 119) or (i == 1 and p == 75):
                    for j, char in enumerate(decrypted_message):
                        decoded_matrix[j].append(char)
        else:
            print(f"第{i + 1}輪次沒有找到合適的密鑰p")

        # 更新prev_c_list為當前的c_list
        prev_c_list = c_list

# 主程序
input_file = 'transposed_data.txt'


# 統計並寫入所有可能的解密結果
decrypt_all_possible_results(input_file)
