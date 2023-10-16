# DGY785
# python3

def modulo_inverse(num, modulo):
    # Calculate the modular inverse of 'num' under 'modulo'
    gcd, x, _ = modified_gcd(num, modulo)
    if gcd == 1:
        return x % modulo
    else:
        return None

def modified_gcd(x, y):
    # Calculate the greatest common divisor (gcd) of 'x' and 'y' along with coefficients
    if x == 0:
        return (y, 0, 1)
    else:
        result, a, b = modified_gcd(y % x, x)
        return (result, b - (y // x) * a, a)

def initialize_inverse_header(header_size):
    # Initialize the inverse header matrix
    inverse_header = [[0] * header_size for _ in range(header_size)]
    for i in range(header_size):
        inverse_header[i][i] = 1  # Initialize the diagonal elements to 1
    return inverse_header

def gaussian_elimination(encoded_data, inverse_header, modulus, header_size):
    # Perform Gauss-Jordan elimination to find the inverse
    for col in range(header_size):
        col_value = modulo_inverse(encoded_data[col][col], modulus)
        for j in range(header_size):
            encoded_data[col][j] = (encoded_data[col][j] * col_value) % modulus
            inverse_header[col][j] = (inverse_header[col][j] * col_value) % modulus
        for row in range(header_size):
            if row != col:
                factor = encoded_data[row][col]
                for i in range(header_size):
                    encoded_data[row][i] = (encoded_data[row][i] - factor * encoded_data[col][i]) % modulus
                    inverse_header[row][i] = (inverse_header[row][i] - factor * inverse_header[col][i]) % modulus
    return inverse_header

def decode_message(encoded_data, gaus_inverse_header, header_size, message_size, modulus):
    # Decode the message parts using the inverse header
    decoded_parts = []
    for i in range(header_size):
        decoded_part = []
        for j in range(message_size):
            decoded_char = 0
            for k in range(header_size):
                decoded_char = (decoded_char + gaus_inverse_header[i][k] * encoded_data[k][header_size + j]) % modulus
            decoded_part.append(decoded_char)
        decoded_parts.append(decoded_part)
    return decoded_parts

def convert_to_text(decoded_parts):
    # Convert the decoded characters to their ASCII representations and concatenate
    decoded_message = ''
    for part in decoded_parts:
        for cr in part:
            decoded_message += chr(cr)
    return decoded_message

def decrypt_message(header_size, message_size, encoded_data, modulus):
    # Initialize the inverse encoding header matrix
    inverse_header = initialize_inverse_header(header_size)
    
    # Perform Gauss-Jordan elimination to find the inverse
    gaus_inverse_header = gaussian_elimination(encoded_data, inverse_header, modulus, header_size)

    # Decode the message parts using the inverse header
    decoded_parts = decode_message(encoded_data, gaus_inverse_header, header_size, message_size, modulus)

    # Convert the decoded characters to their ASCII representations and concatenate
    converted_text = convert_to_text(decoded_parts)

    return converted_text

# Read input
header_size = int(input())
message_size = int(input())
encoded_data = [list(map(ord, input().strip())) for _ in range(header_size)]
modulus = 127

# Decrypt the message
decrypted_message = decrypt_message(header_size, message_size, encoded_data, modulus)

# Print the decrypted message
print(decrypted_message)
