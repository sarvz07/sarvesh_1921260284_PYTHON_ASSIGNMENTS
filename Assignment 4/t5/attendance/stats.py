def present_count(rows):
    return sum(1 for _, status in rows if status == "P")
