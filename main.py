from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Elizabeth")

# Create pets
bella = Pet("Bella", "Dog")
milo = Pet("Milo", "Cat")

owner.add_pet(bella)
owner.add_pet(milo)

# Add tasks out of order
bella.add_task(Task("Morning Walk", "08:00", "daily"))
bella.add_task(Task("Feeding", "07:30"))
milo.add_task(Task("Vet Appointment", "08:00"))  # conflict on purpose

scheduler = Scheduler()

# Sorting
tasks = owner.get_all_tasks()
sorted_tasks = scheduler.sort_by_time(tasks)

print("\n🐾 SORTED SCHEDULE\n")
for pet_name, task in sorted_tasks:
    print(f"{task.time} — {pet_name}: {task.description}")

# Filtering example
print("\n🐾 FILTERED (Bella only)\n")
bella_tasks = scheduler.filter_tasks(tasks, pet_name="Bella")
for pet_name, task in bella_tasks:
    print(f"{task.time} — {pet_name}: {task.description}")

# Conflict detection
print("\n🐾 CONFLICT CHECK\n")
conflicts = scheduler.detect_conflicts(tasks)
if conflicts:
    print("⚠️ Conflicts found:")
    for c1, c2 in conflicts:
        print(f" - {c1[0]} and {c2[0]} both have tasks at {c1[1].time}")
else:
    print("No conflicts detected.")

# Recurrence example
print("\n🐾 RECURRENCE DEMO\n")
task = bella.tasks[0]
task.mark_complete()
scheduler.handle_recurrence(bella)
print(f"New tasks for Bella: {len(bella.tasks)}")
