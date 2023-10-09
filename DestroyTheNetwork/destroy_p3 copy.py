import random
import math

# 计算路径长度
def calculate_path_length(path, distances):
    length = 0
    for i in range(len(path) - 1):
        length += distances[path[i]][path[i + 1]]
    length += distances[path[-1]][path[0]]  # 回到起点
    return length

# 生成初始解
def generate_initial_solution(num_cities):
    return random.sample(range(num_cities), num_cities)

# 2-opt邻域操作
def apply_2_opt(solution, i, j):
    new_solution = solution[:i] + solution[i:j+1][::-1] + solution[j+1:]
    return new_solution

# 模拟退火算法
def simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations):
    num_cities = len(distances)
    current_solution = generate_initial_solution(num_cities)
    current_length = calculate_path_length(current_solution, distances)

    best_solution = current_solution.copy()
    best_length = current_length

    temperature = initial_temperature

    for iteration in range(num_iterations):
        # 生成随机邻域
        i, j = random.sample(range(num_cities), 2)
        new_solution = apply_2_opt(current_solution, i, j)
        new_length = calculate_path_length(new_solution, distances)

        # 计算能量差
        delta_length = new_length - current_length

        # 判断是否接受新解
        if delta_length < 0 or random.random() < math.exp(-delta_length / temperature):
            current_solution = new_solution
            current_length = new_length

            # 更新最优解
            if current_length < best_length:
                best_solution = current_solution.copy()
                best_length = current_length

        # 降低温度
        temperature *= cooling_rate

    return best_solution, best_length

# 示例用法
if __name__ == "__main__":
    num_cities = 10
    distances = [[0 for _ in range(num_cities)] for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distances[i][j] = distances[j][i] = random.randint(1, 100)

    initial_temperature = 90.0
    cooling_rate = 0.55
    num_iterations = 1000

    best_solution, best_length = simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations)

    print("Best Solution:", best_solution)
    print("Best Length:", best_length)