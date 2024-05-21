# word.txt(網路上)
dictionary_file = 'words.txt'
output_file = 'eight_letter_words.txt'

# 篩選出所有8個字母的單詞
def get_8_letter_words(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()

    eight_letter_words = [word for word in words if len(word) == 8]
    return eight_letter_words

# 寫入新的文本文件
def save_words_to_file(words, file):
    with open(file, 'w') as f:
        for word in words:
            f.write(word + '\n')

eight_letter_words = get_8_letter_words(dictionary_file)


save_words_to_file(eight_letter_words, output_file)

print(f"已保存到 {output_file}")
