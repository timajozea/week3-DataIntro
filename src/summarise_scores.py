import statistics as stats


def summarise_scores(scores):
    """Return count, total, and average for a list of scores.

    Example:
        summarise_scores([6, 8, 10])
        {"count": 3, "total": 24, "average": 8.0}
    """
    for score in scores:
        if score is None:
            score = "None"
        else:
            score = score

        count = len(scores)
        total = sum(scores)
        average = stats.mean(scores)

    # Write the function body here.
    statistics = f"""Number of scores recorded: {count}
Sum of the scores: {total}
Average of the scores: {average}"""

    return print(statistics)
