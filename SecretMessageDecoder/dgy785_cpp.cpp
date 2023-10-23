#include <iostream>
#include <vector>
#include <tuple>

std::tuple<int, int, int> modified_gcd(int x, int y);

int modulo_inverse(int num, int modulo) {
    // Calculate the modular inverse of 'num' under 'modulo'
    int gcd, x, _;
    std::tie(gcd, x, _) = modified_gcd(num, modulo);
    if (gcd == 1) {
        return (x % modulo + modulo) % modulo;
    } else {
        return -1;  // Return a value to indicate failure (no modular inverse)
    }
}

std::tuple<int, int, int> modified_gcd(int x, int y) {
    // Calculate the greatest common divisor (gcd) of 'x' and 'y' along with coefficients
    if (x == 0) {
        return std::make_tuple(y, 0, 1);
    } else {
        auto [result, a, b] = modified_gcd(y % x, x);
        return std::make_tuple(result, b - (y / x) * a, a);
    }
}

std::vector<std::vector<int>> initialize_inverse_header(int header_size) {
    // Initialize the inverse header matrix
    std::vector<std::vector<int>> inverse_header(header_size, std::vector<int>(header_size, 0));
    for (int i = 0; i < header_size; ++i) {
        inverse_header[i][i] = 1;  // Initialize the diagonal elements to 1
    }
    return inverse_header;
}

std::vector<std::vector<int>> gaussian_elimination(std::vector<std::vector<int>>& encoded_data, std::vector<std::vector<int>>& inverse_header, int modulus, int header_size) {
    // Perform Gauss-Jordan elimination to find the inverse
    for (int col = 0; col < header_size; ++col) {
        int col_value = modulo_inverse(encoded_data[col][col], modulus);
        for (int j = 0; j < header_size; ++j) {
            encoded_data[col][j] = (encoded_data[col][j] * col_value % modulus + modulus) % modulus;
            inverse_header[col][j] = (inverse_header[col][j] * col_value % modulus + modulus) % modulus;
        }
        for (int row = 0; row < header_size; ++row) {
            if (row != col) {
                int factor = encoded_data[row][col];
                for (int i = 0; i < header_size; ++i) {
                    encoded_data[row][i] = (encoded_data[row][i] - factor * encoded_data[col][i] % modulus + modulus) % modulus;
                    inverse_header[row][i] = (inverse_header[row][i] - factor * inverse_header[col][i] % modulus + modulus) % modulus;
                }
            }
        }
    }
    return inverse_header;
}

std::vector<std::vector<int>> decode_message(std::vector<std::vector<int>>& encoded_data, std::vector<std::vector<int>>& gaus_inverse_header, int header_size, int message_size, int modulus) {
    // Decode the message parts using the inverse header
    std::vector<std::vector<int>> decoded_parts;
    for (int i = 0; i < header_size; ++i) {
        std::vector<int> decoded_part;
        for (int j = 0; j < message_size; ++j) {
            int decoded_char = 0;
            for (int k = 0; k < header_size; ++k) {
                decoded_char = (decoded_char + gaus_inverse_header[i][k] * encoded_data[k][header_size + j] % modulus + modulus) % modulus;
            }
            decoded_part.push_back(decoded_char);
        }
        decoded_parts.push_back(decoded_part);
    }
    return decoded_parts;
}

std::string convert_to_text(std::vector<std::vector<int>>& decoded_parts) {
    // Convert the decoded characters to their ASCII representations and concatenate
    std::string decoded_message;
    for (auto& part : decoded_parts) {
        for (int cr : part) {
            decoded_message += static_cast<char>(cr);
        }
    }
    return decoded_message;
}

std::string decrypt_message(int header_size, int message_size, std::vector<std::vector<int>>& encoded_data, int modulus) {
    // Initialize the inverse encoding header matrix
    auto inverse_header = initialize_inverse_header(header_size);

    // Perform Gauss-Jordan elimination to find the inverse
    auto gaus_inverse_header = gaussian_elimination(encoded_data, inverse_header, modulus, header_size);

    // Decode the message parts using the inverse header
    auto decoded_parts = decode_message(encoded_data, gaus_inverse_header, header_size, message_size, modulus);

    // Convert the decoded characters to their ASCII representations and concatenate
    return convert_to_text(decoded_parts);
}

int main() {
    int header_size, message_size;
    std::cin >> header_size >> message_size;

    std::vector<std::vector<int>> encoded_data(header_size, std::vector<int>(header_size + message_size));

    for (int i = 0; i < header_size; ++i) {
        for (int j = 0; j < header_size + message_size; ++j) {
            char c;
            std::cin >> c;
            encoded_data[i][j] = static_cast<int>(c);
        }
    }

    int modulus = 127;

    // Decrypt the message
    std::string decrypted_message = decrypt_message(header_size, message_size, encoded_data, modulus);

    // Print the decrypted message
    std::cout << decrypted_message << std::endl;

    return 0;
}
