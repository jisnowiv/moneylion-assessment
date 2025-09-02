from boundingBox import *


def test_find_binding_box_simple():
    grid = [
        list("--**---"),
        list("--**---"),
        list("---*---"),
        list("--***--"),
        list("-------"),
        list("***----")
    ]

    expected = [
        (0, 2, 3, 4),
        (5, 0, 5, 2)
    ]

    boxes = find_all_boxes(grid)

    assert sorted(boxes) == sorted(expected)


def test_find_binding_box_single_star():
    grid = [
        list("-----"),
        list("--*--"),
        list("-----")
    ]

    expected = [(1, 2, 1, 2)]
    boxes = find_all_boxes(grid)

    assert boxes == expected


def test_find_binding_box_no_stars():
    grid = [
        list("-----"),
        list("-----"),
        list("-----")
    ]

    boxes = find_all_boxes(grid)
    assert boxes == []


def test_eliminate_overlapping_boxes_removes_inner_box():
    boxes = [
        (0, 0, 3, 3),
        (1, 1, 2, 2),
        (4, 4, 5, 5)
    ]

    expected = [
        (4, 4, 5, 5)
    ]

    result = eliminate_overlapping_boxes(boxes)
    assert sorted(result) == sorted(expected)


def test_eliminate_overlapping_boxes_partial_overlap():
    boxes = [
        (0, 0, 2, 2),
        (1, 1, 3, 3),
        (5, 5, 6, 6)
    ]

    expected = [
        (5, 5, 6, 6)
    ]

    result = eliminate_overlapping_boxes(boxes)
    assert sorted(result) == sorted(expected)


def test_adjust_base():
    box = (0, 1, 2, 3)

    result = adjust_base(box)

    assert result == (1, 2, 3, 4)


def test_find_largest_box_1():
    result = find_largest_box("resources/test1.txt")

    assert result == (2, 2, 3, 3)


def test_find_largest_box_2():
    result = find_largest_box("resources/test2.txt")

    assert result == (1, 1, 2, 2)


def test_find_largest_box_none():
    result = find_largest_box("resources/test3.txt")

    assert not result
