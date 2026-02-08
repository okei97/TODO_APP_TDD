import uuid
MAX_TITLE_LENGTH = 100

class Todo:
    def __init__(self, title: str, id: str | None = None):
        if not title:
            raise ValueError("title is required")
        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError(f"title must be less than or equal to {MAX_TITLE_LENGTH} characters")
        self.title = title
        self.id = id or str(uuid.uuid4())
        self.completed = False