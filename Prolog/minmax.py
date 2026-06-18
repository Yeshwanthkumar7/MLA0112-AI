import math

def minimax(depth, node_index, is_max, values, max_depth):
    if depth == max_depth:
        return values[node_index], [chr(65 + node_index)]

    if is_max:
        left_val, left_path = minimax(depth + 1, 2 * node_index, False, values, max_depth)
        right_val, right_path = minimax(depth + 1, 2 * node_index + 1, False, values, max_depth)

        if left_val >= right_val:
            return left_val, [chr(65 + node_index)] + left_path
        else:
            return right_val, [chr(65 + node_index)] + right_path

    else:
        left_val, left_path = minimax(depth + 1, 2 * node_index, True, values, max_depth)
        right_val, right_path = minimax(depth + 1, 2 * node_index + 1, True, values, max_depth)

        if left_val <= right_val:
            return left_val, [chr(65 + node_index)] + left_path
        else:
            return right_val, [chr(65 + node_index)] + right_path


values = [3, 5, 2, 9, 12, 5, 23, 23]
max_depth = int(math.log2(len(values)))

optimal_value, path = minimax(0, 0, True, values, max_depth)

print("Optimal Value:", optimal_value)
print("Path:", " -> ".join(path))