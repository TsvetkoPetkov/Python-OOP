from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        is_capacity_enough = self.__animal_capacity > len(self.animals)
        is_budget_enough = self.__budget >= price

        if is_capacity_enough and is_budget_enough:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_capacity_enough and not is_budget_enough:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum([c.salary for c in self.workers])

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = sum([m.money_for_care for m in self.animals])
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"

        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"

        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result.strip()

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"

        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"

        for keeper in keepers:
            result += f"{keeper}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"

        for caretaker in caretakers:
            result += f"{caretaker}\n"

        result += f"----- {len(vets)} Vets:\n"

        for vet in vets:
            result += f"{vet}\n"

        return result.strip()