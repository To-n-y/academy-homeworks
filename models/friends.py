class Friends:
    first_id: int
    second_id: int

    def __init__(self, first_id, second_id):
        self.first_id = first_id
        self.second_id = second_id

    def __str__(self):
        return f"Friends(first_id={self.first_id}, second_id={self.second_id})"
