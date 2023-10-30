def calculate_average_traffic(packet_size_bytes, packet_interval_ms):
    # Convert packet interval from milliseconds to seconds
    packet_interval_seconds = packet_interval_ms / 1000
    
    # Calculate the average rate in bits per second (bps)
    average_rate_bps = (packet_size_bytes * 8) / packet_interval_seconds
    
    return average_rate_bps

def calculate_total_traffic(n):
    # Define the constants
    active_60_percent = 0.3
    active_50_percent = 0.7
    average_rate_bps = 12000  # The average rate per user in bps

    # Calculate the total traffic
    total_traffic_bps = (active_60_percent * average_rate_bps * n * 0.6) + (active_50_percent * average_rate_bps * n * 0.5)
    
    return total_traffic_bps

import math

import math

def estimate_min_packets(epsilon, loss_requirement):
    """
    Estimate the minimum number of packets (trials) required to fulfill a loss requirement (p) using the Hoeffding formula.

    Parameters:
    - epsilon: The maximum allowable deviation.
    - loss_requirement: The loss requirement (maximum acceptable loss probability).

    Returns:
    - min_packets: The estimated minimum number of packets required.
    """
    min_packets = (1 / (2 * epsilon**2)) * math.log(2 / loss_requirement)
    return min_packets


import math

def estimate_min_capacity(n, epsilon, loss_requirement):
    min_packets = estimate_min_packets(epsilon, loss_requirement)
    min_capacity_kb_s = math.ceil(min_packets / n)  # Round up to the nearest KB/s
    return min_capacity_kb_s


packet_size = 30
packet_interval = 20
average_traffic_rate = calculate_average_traffic(packet_size, packet_interval)
print(f"Average Traffic Rate: {average_traffic_rate} bps")

num_users = 100  # Replace with the actual number of VoIP users
total_traffic = calculate_total_traffic(num_users)
print(f"Total Traffic for {num_users} Users: {total_traffic} bps")

epsilon = 0.01  # Replace with your desired epsilon
loss_requirement = 0.01  # Replace with your desired loss requirement

min_packets = estimate_min_packets(epsilon, loss_requirement)
print(f"Minimum Number of Packets Required: {min_packets}")


n = 100  # Replace with the actual number of users
epsilon = 0.01  # Replace with your desired epsilon
loss_requirement = 0.01  # Replace with your desired loss requirement

min_capacity = estimate_min_capacity(n, epsilon, loss_requirement)
print(f"Minimum Capacity: {min_capacity} KB/s")
