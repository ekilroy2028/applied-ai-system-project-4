from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple
import json
from pathlib import Path


# -----------------------------
# Task Class (Updated for Priority)
# -----------------------------
@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"      # once, daily, weekly
    completed: bool = False
    priority: str = "Medium"     # NEW FIELD: High, Medium, Low

    def mark_complete(self):
        self.completed = True

    def next_occurrence(self):
        """Return the next occurrence time for recurring tasks."""
        if self.frequency == "daily":
            return self.time
        elif self.frequency == "weekly":
            return self.time
        return None


# -----------------------------
# Pet Class
# -----------------------------
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = None

    def __post_init__(self):
        if self.tasks is None:
            self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


# -----------------------------
# Owner Class (with JSON Persistence)
# -----------------------------
@dataclass
class Owner:
    name: str
    pets: List[Pet] = None

    def __post_init__(self):
        if self.pets is None:
            self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Tuple[str, Task]]:
        """Return list of (pet_name, task) pairs."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks

    # -----------------------------
    # JSON Persistence
    # -----------------------------
    def to_dict(self):
        return {
            "name": self.name,
            "pets": [
                {
                    "name": p.name,
                    "species": p.species,
                    "tasks": [
                        {
                            "description": t.description,
                            "time": t.time,
                            "frequency": t.frequency,
                            "completed": t.completed,
                            "priority": t.priority,
                        }
                        for t in p.tasks
                    ],
                }
                for p in self.pets
            ],
        }

    @classmethod
    def from_dict(cls, data):
        owner = cls(data["name"])
        for p_data in data.get("pets", []):
            pet = Pet(p_data["name"], p_data["species"])
            for t_data in p_data.get("tasks", []):
                pet.add_task(
                    Task(
                        t_data["description"],
                        t_data["time"],
                        t_data.get("frequency", "once"),
                        t_data.get("completed", False),
                        t_data.get("priority", "Medium"),
                    )
                )
            owner.add_pet(pet)
        return owner

    def save_to_json(self, path="data.json"):
        Path(path).write_text(json.dumps(self.to_dict(), indent=2))

    @classmethod
    def load_from_json(cls, path="data.json"):
        p = Path(path)
        if not p.exists():
            return None
        data = json.loads(p.read_text())
        return cls.from_dict(data)


# -----------------------------
# Scheduler Class
# -----------------------------
class Scheduler:

    # Priority + Time Sorting (Challenge 3)
    @staticmethod
    def sort_by_priority_then_time(tasks):
        """Sort tasks by priority first, then by time."""
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        fmt = "%H:%M"

        return sorted(
            tasks,
            key=lambda t: (
                priority_order.get(t[1].priority, 1),
                datetime.strptime(t[1].time, fmt),
            ),
        )

    # Original time-only sorting (still available if needed)
    @staticmethod
    def sort_by_time(tasks):
        fmt = "%H:%M"
        return sorted(tasks, key=lambda t: datetime.strptime(t[1].time, fmt))

    # Filtering
    @staticmethod
    def filter_tasks(tasks, pet_name=None, completed=None):
        filtered = []
        for p, t in tasks:
            if pet_name and p != pet_name:
                continue
            if completed is not None and t.completed != completed:
                continue
            filtered.append((p, t))
        return filtered

    # Conflict Detection
    @staticmethod
    def detect_conflicts(tasks):
        seen = {}
        conflicts = []
        for pet_name, task in tasks:
            if task.time in seen:
                conflicts.append((seen[task.time], (pet_name, task)))
            else:
                seen[task.time] = (pet_name, task)
        return conflicts

    # Recurrence Handling
    @staticmethod
    def handle_recurrence(pet: Pet):
        new_tasks = []
        for task in pet.tasks:
            if task.completed and task.frequency in ("daily", "weekly"):
                next_time = task.next_occurrence()
                if next_time:
                    new_tasks.append(
                        Task(
                            task.description,
                            next_time,
                            task.frequency,
                            False,
                            task.priority,
                        )
                    )
        pet.tasks.extend(new_tasks)
        return len(new_tasks)