import sys

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def read_grid(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]


def dfs(grid, visited, r, c, row_count, col_count, bounds):
    stack = [(r, c)]
    visited.add((r, c))

    while stack:
        x, y = stack.pop()
        bounds[0] = min(bounds[0], x)
        bounds[1] = min(bounds[1], y)
        bounds[2] = max(bounds[2], x)
        bounds[3] = max(bounds[3], y)

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < row_count and 0 <= ny < col_count:
                if grid[nx][ny] == '*' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))


def find_all_boxes(grid):
    visited = set()
    boxes = []

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '*' and (r, c) not in visited:
                bounds = [r, c, r, c]
                dfs(grid, visited, r, c, rows, cols, bounds)
                boxes.append(tuple(bounds))

    return boxes


def area(box):
    return (box[2] - box[0] + 1) * (box[3] - box[1] + 1)


def boxes_overlap(b1, b2):
    return not (
        b1[2] < b2[0] or
        b2[2] < b1[0] or
        b1[3] < b2[1] or
        b2[3] < b1[1]
    )


def eliminate_overlapping_boxes(boxes):
    non_overlapping = []
    boxes = sorted(boxes, key=area, reverse=True)

    for i, b1 in enumerate(boxes):
        overlap = False
        for j, b2 in enumerate(boxes):
            if i != j and boxes_overlap(b1, b2):
                overlap = True
                break
        if not overlap:
            non_overlapping.append(b1)

    return non_overlapping


def adjust_base(box: tuple):
    return tuple(map(lambda x: x + 1, box))


def find_largest_box(filename):
    full_grid = read_grid(filename)
    all_boxes = find_all_boxes(full_grid)
    unique_boxes = eliminate_overlapping_boxes(all_boxes)
    return adjust_base((unique_boxes[0])) if len(unique_boxes) > 0 else None


if __name__ == '__main__': # pragma: no cover
    if len(sys.argv) < 2:
        print("Usage: python boundingBox.py <text file>")

    corners = find_largest_box(sys.argv[1])
    if corners:
        print(f"({corners[0]}, {corners[1]}) ({corners[2]}, {corners[3]})")
