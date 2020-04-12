def solver(grid):
    size = grid.size ** 4

    # Building the possibilities grid:
    completion = 0.0
    possibilities_grid = []
    for index in range(size):
        if grid.is_completed(index):
            possibilities_grid.append(None)
            completion += 1
            continue
        possibilities_grid.append(grid.accepted_numbers.copy())
    initial_nb_completed = completion

    # Filling the grid until complete or stuck:
    iterations = 0
    while completion < size:
        previous_completion = completion
        for index, possibilities in enumerate(possibilities_grid):
            if possibilities is None:
                continue

            new_possibilities = []
            for proposition in possibilities:
                if grid.is_valid(index, proposition):
                    new_possibilities.append(proposition)

            completion += 1/(grid.size**2-1) * (len(possibilities)-len(new_possibilities))

            if len(new_possibilities) == 1:
                grid.set_nb(index, new_possibilities[0])
                possibilities_grid[index] = None
                continue

            possibilities_grid[index] = new_possibilities

        iterations += 1

        if previous_completion == completion:
            print(f"Got stuck. Took it from {initial_nb_completed*100/size:.1f}% "
                  f"to {completion*100/size:.1f}% completed over {iterations} iterations.")
            print(possibilities_grid)
            break
