class Todo:
    def __init__(self, title: str):
        if not title:
            raise ValueError("title is required")
        self.title = title
        self.completed = False