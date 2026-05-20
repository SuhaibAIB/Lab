def process_data(numbers, threshold=0):
    """Filter, deduplicate, sort, and transform number data.

    Args:
        numbers (list[int] | list[float]): A list of numeric values.
        threshold (int | float, optional): Minimum value to keep. Defaults to 0.

    Returns:
        list[int] | list[float]: The top 3 unique values above the threshold,
        sorted descending and doubled.
    """
    if not numbers:
        return []

    filtered = [n for n in numbers if n > threshold]
    unique = list(set(filtered))
    sorted_nums = sorted(unique, reverse=True)
    return [n * 2 for n in sorted_nums[:3]]