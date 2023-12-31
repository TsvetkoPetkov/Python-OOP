class Trainer:
    id = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Trainer.id
        Trainer.id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id() -> int:
        return Trainer.id