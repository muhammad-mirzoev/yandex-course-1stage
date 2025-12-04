def find_farthest_orbit(list_of_orbits):
    return max(
        ((a, b) for a, b in list_of_orbits if a != b),
        key=lambda orbit: orbit[0] * orbit[1]
    )


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
