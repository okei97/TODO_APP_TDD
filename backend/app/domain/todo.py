import uuid
from datetime import datetime
MAX_TITLE_LENGTH = 100

class Todo:
    def __init__(self, title: str, id: str | None = None): #idは外部から指定できなくてもいいから、引数から削除する？
        if not title:
            raise ValueError("title is required")
        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError(f"title must be less than or equal to {MAX_TITLE_LENGTH} characters")
        self.title = title
        self.id = id or str(uuid.uuid4())
        self.completed = False
        self.completed_at: datetime | None = None

    def complete(self, now: datetime):
        if self.completed:
            raise ValueError("Todo is already completed")
        self.completed = True
        self.completed_at = now
    
    # 実装しないコメントアウトする
    def uncomplete(self):
        if not self.completed:
            raise ValueError("Todo is already incomplete")
        self.completed = False