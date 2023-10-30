import math

# Packet loss probability requirement
P = 0.01

# Number of users
n = 100

# Packet size in bytes
packet_size = 30

# Initialize capacity
capacity = 1  # Starting with 1 KB/s

# Tolerance for capacity estimation
tolerance = 0.001

while True:
    # Calculate N using the Hoeffding formula
    N = -math.log(P) / (2 * n * (packet_size / capacity))

    # Calculate capacity in KB/s
    capacity_kb = (n * packet_size) / (N * 1024)

    # Check if the capacity fulfills the requirement
    if capacity_kb >= capacity:
        break
    else:
        # Increment capacity
        capacity += tolerance

print(f"Minimum capacity: {capacity} KB/s (rounded to nearest 1 KB/s)")
