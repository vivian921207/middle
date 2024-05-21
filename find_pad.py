def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)
def text_to_ascii_bytes(text):
    return bytes(text, 'ascii')
def calculate_pad_one_time_pad(plaintext, ciphertext):
    # Ensure the input lengths match
    assert len(plaintext) == len(ciphertext)
    pad = bytes([p ^ c for p, c in zip(plaintext, ciphertext)])
    return pad


def calculate_pad_feedback(plaintext, ciphertext):
    # Ensure the input lengths match
    #assert len(plaintext) == len(ciphertext)
    pad = []
    prev_c = 0
    for m, c in zip(plaintext, ciphertext):
        for p in range(256):
            mi = (c ^ (p + prev_c) % 256)
            if mi==m:
                pad.append(p)
                prev_c = c
                break
    return bytes(pad)

# 已知明文和密文
plaintext1 = text_to_ascii_bytes("We stand today on the brink of a revolution in cryptography.")
ciphertext1 = [32, 14, 162, 166, 143, 97, 199, 84, 128, 186, 67, 246, 43, 37, 76, 222, 75, 131, 131, 185, 79, 149, 100, 201, 116, 219, 101, 188, 112, 206, 25, 63, 147, 142, 153, 112, 190, 67, 231, 37, 246, 85, 249, 123, 161, 135, 215, 124, 193, 143, 135, 201, 67, 237, 54, 246, 74, 196, 77, 80]

# 計算pad for classical One-Time Pad
#pad1 = calculate_pad_one_time_pad(plaintext1, ciphertext1)
#print("Classical One-Time Pad:", pad1.hex())

# 計算pad for One-Time Pad with Feedback
pad2 = calculate_pad_feedback(plaintext1, ciphertext1)
print("One-Time Pad with Feedback:", pad2.hex())
