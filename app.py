import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# -----------------------------
# Session State Initialization
# -----------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Elizabeth")

owner = st.session_state.owner
scheduler = Scheduler()

st.title("🐾 PawPal+")

# -----------------------------
# Add a Pet
# -----------------------------
st.subheader("Add a New Pet")

with st.form("add_pet"):
    name = st.text_input("Pet Name")
    species = st.text_input("Species")
    submitted = st.form_submit_button("Add Pet")

    if submitted:
        if name and species:
            owner.add_pet(Pet(name, species))
            st.success(f"Added {name} the {species}!")
        else:
            st.error("Please enter both a name and species.")

# -----------------------------
# Add a Task
# -----------------------------
if owner.pets:
    st.subheader("Add a Task")

    with st.form("add_task"):
        pet_name = st.selectbox("Choose Pet", [p.name for p in owner.pets])
        desc = st.text_input("Task Description")
        time = st.time_input("Time")
        freq = st.selectbox("Frequency", ["once", "daily", "weekly"])
        submitted = st.form_submit_button("Add Task")

        if submitted:
            pet = next(p for p in owner.pets if p.name == pet_name)
            pet.add_task(Task(desc, time.strftime("%H:%M"), freq))
            st.success(f"Added task for {pet_name}!")
else:
    st.info("Add a pet first to begin scheduling tasks.")

# -----------------------------
# Display Today's Schedule
# -----------------------------
st.subheader("Today's Schedule")

tasks = owner.get_all_tasks()
sorted_tasks = scheduler.sort_by_time(tasks)

if sorted_tasks:
    for pet_name, task in sorted_tasks:
        st.write(f"**{task.time}** — {pet_name}: {task.description}")
else:
    st.info("No tasks scheduled yet.")

# -----------------------------
# Conflict Detection
# -----------------------------
conflicts = scheduler.detect_conflicts(tasks)

if conflicts:
    st.warning("⚠️ Task conflicts detected!")
    for (p1, t1), (p2, t2) in conflicts:
        st.write(f"- {p1} and {p2} both have tasks at **{t1.time}**")



# -----------------------------
#Challenge 4: Professional UI and Output Formatting
# -----------------------------

PRIORITY_EMOJI = {
    "High": "🔴",
    "Medium": "🟡",
    "Low": "🟢",
}

FREQUENCY_EMOJI = {
    "daily": "📅",
    "weekly": "🗓️",
    "once": "⏳",
}

