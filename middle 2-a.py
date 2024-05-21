import itertools

# 原本
hex_numbers_1 = ["e9", "3a", "e9", "c5", "fc", "73", "55", "d5"]
hex_numbers_2 = ["f4", "3a", "fe", "c7", "e1", "68", "4a", "df"]

# 10進制
dec_numbers_1 = [int(num, 16) for num in hex_numbers_1]
dec_numbers_2 = [int(num, 16) for num in hex_numbers_2]

# 異或
c = [dec_numbers_1[i] ^ dec_numbers_2[i] for i in range(8)]

# 結果
print("第一組 16進制數字轉為10進制：", dec_numbers_1)
print("第二組 16進制數字轉為10進制：", dec_numbers_2)
print("前八個數字的異或結果：", c)

# 讀取所有8個字母單詞
def get_8_letter_words(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()
    return words

# 輸出結果到結果
def save_words_to_file(words, file):
    with open(file, 'w') as f:
        for word in words:
            f.write(word + '\n')

# 檢查是否也為英文單詞的組合
def check_and_output_valid_results(words, c):
    valid_results = []
    for word in words:
        xor_result = [ord(word[i]) ^ c[i] for i in range(8)]
        result = ''.join(chr(x) for x in xor_result)
        if result in words:
            valid_results.append(result)
    return valid_results

# 讀取文件
dictionary_file = 'eight_letter_words.txt'
eight_letter_words = get_8_letter_words(dictionary_file)

valid_results = check_and_output_valid_results(eight_letter_words, c)
print(valid_results)

