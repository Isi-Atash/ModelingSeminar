#RMPSYJ
#python3

def inverse_modulo(num, modulo):
    for i in range(1, modulo):
        if (i * num) % modulo == 1:
            return i
    return None

def decode_message(hs, ms, encoded_parts):
    # Initialize the inverse encoding header matrix
    inverse_header = [[0] * hs for _ in range(hs)]
    for i in range(hs):
        inverse_header[i][i] = 1  # Initialize the diagonal elements to 1

    # Perform Gauss-Jordan elimination to find the inverse
    for col in range(hs):
        col_val = inverse_modulo(encoded_parts[col][col], 127)
        for j in range(hs):
            encoded_parts[col][j] = (encoded_parts[col][j] * col_val) % 127  #multiple by the inverse modulo of the diag value mod 127
            inverse_header[col][j] = (inverse_header[col][j] * col_val) % 127
        for row in range(hs):
            if row != col:
                factor = encoded_parts[row][col]
                for i in range(hs):
                    encoded_parts[row][i] = (encoded_parts[row][i] - factor * encoded_parts[col][i]) % 127
                    inverse_header[row][i] = (inverse_header[row][i] - factor * inverse_header[col][i]) % 127

    # Decode the message parts using the inverse header
    decoded_parts = []
    for i in range(hs):
        decoded_part = []
        for j in range(ms):
            decoded_char = 0
            for k in range(hs):
                decoded_char = (decoded_char + inverse_header[i][k] * encoded_parts[k][hs + j]) % 127
            decoded_part.append(decoded_char)
        decoded_parts.append(decoded_part)

    # Convert the decoded characters to their ASCII representations and concatenate
    decoded_message = ''
    for part in decoded_parts:
        for cr in part:
            decoded_message += chr(cr)
    return decoded_message

# Read input
hs = int(input())
ms = int(input())
encoded_parts = [list(map(ord, input().strip())) for _ in range(hs)]

# Decode the message
decoded_message = decode_message(hs, ms, encoded_parts)

# Print the decoded message
print(decoded_message)