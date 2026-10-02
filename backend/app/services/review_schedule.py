# This file keeps the spaced-review schedule in one place.

# Set the number of days until each next review.
REVIEW_INTERVAL_DAYS = (
    1,
    3,
    7,
    14,
    30,
)


def get_next_review_days(review_count: int) -> int:
    # Keep negative values safe.
    safe_review_count = max(review_count, 0)

    # Keep later reviews on the final 30-day interval.
    interval_index = min(
        safe_review_count,
        len(REVIEW_INTERVAL_DAYS) - 1,
    )

    # Send the number of days for the next review.
    return REVIEW_INTERVAL_DAYS[interval_index]
