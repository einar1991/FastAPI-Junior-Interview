# Debugging
# Understand what this function does and fix it
def find_user_by_email(users: list[dict], email: str) -> dict | None:
    for user in users:
        if email in users:
            return user


# Fixed
def find_user_by_email(users: list[dict], email: str) -> dict | None:
    if not users or not email:
        return None

    for user in users:
        if user.get("email") == email:
            return user

    return None


# Business logic
# Create a class for managing user's history
class UserActionHistory:
    def __init__(self):
        self.history = []

    def add_action(self, action_type: str) -> None:
        pass

    def get_recent_actions(self, n: int = 10) -> list:
        pass

    def get_top_actions(self, n: int = 3) -> list[tuple[str, int]]:
        """
        Return N of the most frequent actions and how many times have they been found.

        Example:
        history = ['login', 'login', 'view', 'login', 'view', 'buy']
        get_top_actions(2) -> [('login', 3), ('view', 2)]

        Sort by frequency, then by alphabet
        """
        pass


# Solution
class UserActionHistory:
    """
    Create a class for managing user's history
    """

    def __init__(self):
        self.history = []

    def add_action(self, action_type: str):
        self.history.append(action_type)

    def get_recent_actions(self, n: int = 10) -> list:
        return self.history[-n:] if n > 0 else []

    def get_top_actions(self, n: int = 3) -> list[tuple[str, int]]:
        """
        Return N of the most frequent actions and how many times have they been found.

        Example:
        history = ['login', 'login', 'view', 'login', 'view', 'buy']
        get_top_actions(2) -> [('login', 3), ('view', 2)]

        Sort by frequency, then by alphabet
        """
        if n <= 0 or not self.history:
            return []

        action_counts = {}
        for action in self.history:
            action_counts[action] = action_counts.get(action, 0) + 1

        sorted_actions = sorted(action_counts.items(), key=lambda x: (-x[1], x[0]))

        return sorted_actions[:n]
