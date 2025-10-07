def is_terminal(node):
    # Check if node is a number (leaf node)
    return not isinstance(node, list)

def heuristic_value(node):
    # Return the value of a leaf node
    return node

def get_children(node):
    return node

def alpha_beta(node, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or is_terminal(node):
        return heuristic_value(node)
    
    if is_maximizing_player:
        best_value = -1000000  # very small number (negative infinity)
        for child in get_children(node):
            val = alpha_beta(child, depth-1, alpha, beta, False)
            if val > best_value:
                best_value = val
            if best_value > alpha:
                alpha = best_value
            # Prune if beta <= alpha
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = 1000000  # very large number (infinity)
        for child in get_children(node):
            val = alpha_beta(child, depth-1, alpha, beta, True)
            if val < best_value:
                best_value = val
            if best_value < beta:
                beta = best_value
            # Prune if beta <= alpha
            if beta <= alpha:
                break
        return best_value

game_tree = [
    [3, 5],  # First branch
    [6, 9]   # Second branch
]

optimal = alpha_beta(game_tree, depth=3, alpha=-1000000, beta=1000000, is_maximizing_player=True)
print("Optimal value (with Alpha-Beta Pruning):", optimal)


