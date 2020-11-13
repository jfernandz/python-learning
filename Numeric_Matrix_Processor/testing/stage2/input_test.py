def input_dimension():
    try:
        rows, cols = map(int, input().split())
        return rows, cols
    except (TypeError, ValueError):
        print("You must specify rows x columns.")
        return input_dimension()


row, cols = input_dimension()
