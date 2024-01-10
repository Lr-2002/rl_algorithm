import math

def minmax(
        curDepth, nodeIndex,
        maxTurn, scores,
        targetDepth
):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        x = max(minmax(curDepth+1, nodeIndex*2, False, scores, targetDepth),
                minmax(curDepth+1, nodeIndex*2+1, False, scores, targetDepth))
        print(f'depth: {curDepth}, node: {nodeIndex}, scores = {x}')
        return x
    else:
        x = min(minmax(curDepth+1, nodeIndex*2, True, scores, targetDepth),
                minmax(curDepth+1, nodeIndex*2+1, True, scores, targetDepth))
        print(f'depth: {curDepth}, node: {nodeIndex}, scores = {x}')
        return x


def visualize_tree(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return

    prefix = "    " * curDepth
    if maxTurn:
        print(f"{prefix}Max Node {nodeIndex}, scores = {scores[nodeIndex]}")
    else:
        print(f"{prefix}Min Node {nodeIndex}, scores = {scores[nodeIndex]}")

    visualize_tree(curDepth + 1, nodeIndex * 2, not maxTurn, scores, targetDepth)
    visualize_tree(curDepth + 1, nodeIndex * 2 + 1, not maxTurn, scores, targetDepth)


if __name__ == '__main__':
    scores = [3, 5, 2, 9, 12, 5, 23, 23]

    treeDepth = int(math.log2(len(scores)))

    print("Initial Tree:")
    visualize_tree(0, 0, True, scores, treeDepth)

    print("\nMinimax Result:", minmax(0, 0, True, scores, treeDepth))
