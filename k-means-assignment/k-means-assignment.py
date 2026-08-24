def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    assignments = []

    for point in points:
        distances = []

        for centroid in centroids:
            distance = sum(
                (p - c) ** 2
                for p, c in zip(point, centroid)
            )
            distances.append(distance)

        assignments.append(distances.index(min(distances)))

    return assignments