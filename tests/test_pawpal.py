from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    """Task Completion: mark_complete() should set completed to True."""
    task = Task("Walk", "08:00")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    """Task Addition: adding a task should increase the pet's task count."""
    pet = Pet("Bella", "Dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task("Walk", "08:00"))
    assert len(pet.tasks) == 1


def test_sorting_correctness():
    """Sorting: tasks should be returned in chronological order."""
    tasks = [
        ("Bella", Task("Walk", "09:00")),
        ("Bella", Task("Feeding", "07:00")),
        ("Bella", Task("Playtime", "08:00")),
    ]
    sorted_tasks = Scheduler.sort_by_time(tasks)
    assert [t[1].time for t in sorted_tasks] == ["07:00", "08:00", "09:00"]


def test_recurrence_logic_daily():
    """Recurrence: completing a daily task should create a new task."""
    pet = Pet("Bella", "Dog")
    task = Task("Walk", "08:00", "daily")
    pet.add_task(task)

    task.mark_complete()
    Scheduler.handle_recurrence(pet)

    assert len(pet.tasks) == 2  # original + new occurrence
    assert pet.tasks[1].description == "Walk"
    assert pet.tasks[1].time == "08:00"


def test_conflict_detection():
    """Conflict Detection: tasks with the same time should be flagged."""
    tasks = [
        ("Bella", Task("Walk", "08:00")),
        ("Milo", Task("Vet", "08:00")),
    ]
    conflicts = Scheduler.detect_conflicts(tasks)
    assert len(conflicts) == 1


def test_filter_by_pet_name():
    """Filtering: only tasks for the specified pet should be returned."""
    tasks = [
        ("Bella", Task("Walk", "08:00")),
        ("Milo", Task("Vet", "09:00")),
    ]
    filtered = Scheduler.filter_tasks(tasks, pet_name="Bella")
    assert len(filtered) == 1
    assert filtered[0][0] == "Bella"


def test_filter_by_completion_status():
    """Filtering: only completed tasks should be returned."""
    t1 = Task("Walk", "08:00")
    t2 = Task("Vet", "09:00")
    t2.mark_complete()

    tasks = [("Bella", t1), ("Milo", t2)]
    filtered = Scheduler.filter_tasks(tasks, completed=True)

    assert len(filtered) == 1
    assert filtered[0][1].completed is True
