classDiagram
    class Task {
        +str description
        +str time
        +str frequency
        +bool completed
        +mark_complete()
        +next_occurrence()
    }

    class Pet {
        +str name
        +str species
        +List~Task~ tasks
        +add_task(task)
        +get_tasks()
    }

    class Owner {
        +str name
        +List~Pet~ pets
        +add_pet(pet)
        +get_all_tasks()
    }

    class Scheduler {
        +sort_by_time(tasks)
        +filter_tasks(tasks, pet_name, completed)
        +detect_conflicts(tasks)
        +handle_recurrence(pet)
    }

    Owner --> Pet : owns >
    Pet --> Task : has >
    Scheduler --> Owner : reads tasks >
