# Debugging
# Understand what this function does and fix it
def find_user_by_email(users: list[dict], email: str) -> dict | None:
    for user in users:
        if email in users:
            return user


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
