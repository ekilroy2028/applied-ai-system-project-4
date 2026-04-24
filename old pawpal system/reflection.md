# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial design centered on four core classes: **Owner**, **Pet**, **Task**, and **Scheduler**. I wanted a clean separation of responsibilities: Owners manage pets, pets manage tasks, and the Scheduler handles all the “thinking” — sorting, filtering, conflict detection, and recurrence. This structure felt intuitive and aligned well with the real-world relationships the app 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
As I moved from UML to implementation, I made a few adjustments. The biggest shift was simplifying the Scheduler so it never stores state; instead, it operates purely on data passed into it. Copilot initially suggested embedding scheduling logic inside the Owner class, but that felt like a violation of separation of concerns. I kept the logic centralized and modular, which made testing and UI integration much cleaner.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
To make the scheduler feel genuinely useful rather than just a container for tasks, I implemented four core algorithmic features: sorting, filtering, recurrence, and conflict detection. Each one addressed a specific limitation I noticed during the CLI-first testing phase.

**Sorting** was the first improvement. Without it, tasks appeared in the order they were added, which felt arbitrary and unhelpful. Implementing a time-based sort using `datetime.strptime` immediately made the schedule feel more like a real agenda.

**Filtering** came next. As soon as I added multiple pets and several tasks, it became clear that I needed a way to view tasks by pet or by completion status. The filtering method is intentionally simple—just a couple of list comprehensions—but it adds a lot of usability.

**Recurring tasks** were the most interesting feature to design. I wanted the system to feel “alive,” meaning that completing a daily or weekly task should automatically generate the next occurrence. I kept the recurrence logic lightweight by reusing the same time and description, which works well for predictable routines like feeding or walks.

Finally, **conflict detection** helps surface potential scheduling issues. The algorithm checks for tasks that share the same time and returns pairs of conflicts. It’s not a full calendar engine, but it’s enough to warn the user when two pets need attention simultaneously.

Together, these features transform PawPal+ from a static list manager into a small but capable scheduling assistant.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff I made in the scheduling logic was keeping conflict detection intentionally simple. The system only checks for exact time matches, not overlapping durations or multi-step tasks. This keeps the algorithm lightweight and easy to understand, but it means the scheduler won’t catch more complex conflicts. For the scope of this project, clarity and maintainability felt more important than implementing a full calendar-style overlap engine.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

Throughout this project, I used AI as a collaborative partner rather than a code generator. I relied on it for several different phases of the workflow: brainstorming the initial class design, clarifying how the Scheduler should interact with the Owner and Pet classes, debugging issues in my logic, and refining my Streamlit UI. Prompts that asked the AI to compare options or explain tradeoffs were especially helpful. For example, asking “What’s a lightweight way to detect task conflicts?” produced a simple dictionary‑based approach that was easy to understand and implement.

I also found that prompts like “Explain why this test is failing” or “Show me a more readable version of this method” helped me understand the reasoning behind the suggestions instead of just copying code. The most helpful prompts were the ones where I asked the AI to reason about structure, not just produce code.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
One moment where I didn’t accept an AI suggestion as‑is was during the recurrence logic. The AI initially suggested adding date arithmetic and storing full datetime objects for each task. While that would be more realistic, it was far more complex than the project required. I evaluated the suggestion by checking the assignment scope and considering how much additional code it would introduce. I ultimately chose a simpler version that regenerates the next daily or weekly task using the same time, which kept the system lightweight and easy to test.

In general, I verified AI suggestions by running them through my own reasoning:

Does this match the project requirements?

Is it readable and maintainable?

Will it complicate testing?

Does it introduce unnecessary features?

This helped me stay in control of the design rather than letting the AI over‑engineer the system.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I wrote tests for the core behaviors that define the scheduler’s correctness: task completion, adding tasks to pets, sorting tasks by time, generating recurring tasks, filtering, and detecting conflicts. These tests were important because they validated the “smart” parts of the system—the logic that transforms PawPal+ from a simple list manager into an actual scheduling assistant. Sorting and conflict detection were especially important to test because they directly affect the user’s experience and could easily break if the time format or data structure changed.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I’m fairly confident (around 4 out of 5) that the scheduler works correctly for the scenarios it was designed for. The tests cover the main behaviors and edge cases like duplicate times and filtering by completion. If I had more time, I would test more complex scenarios such as overlapping durations, multiple recurring tasks triggering at once, or tasks with invalid time formats. I would also add tests for the Streamlit UI logic, even though that’s harder to automate.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I’m most satisfied with how the system architecture evolved. The UML diagram gave me a strong foundation, and the final implementation stayed surprisingly close to the original design. The Scheduler class ended up being the “brain” of the system exactly as intended, and the Streamlit UI felt clean and responsive once I connected it to the logic layer. I also appreciated how the CLI‑first workflow made debugging much easier before touching the UI.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would redesign the task model to include actual dates or durations. Right now, the system only checks for exact time matches, which is fine for the assignment but not realistic for real scheduling. I would also consider adding priority levels or a more sophisticated conflict‑resolution strategy. On the UI side, I would improve the layout and add icons or color‑coding to make the schedule more visually intuitive.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
The biggest thing I learned is that AI is most effective when I treat it as a collaborator, not an answer machine. It’s great at generating options, explaining tradeoffs, and helping me think through design decisions, but I still have to make the final call. This project reinforced the importance of understanding my own system deeply enough to evaluate AI suggestions rather than accepting them blindly. It also showed me how valuable it is to design first, test early, and let the UI come last.

-Copilot suggested combining scheduling logic into the Pet class, but I kept a separate Scheduler class to maintain clean separation of concerns.

✔ Organization

Using separate chat sessions helped me focus on one phase at a time and avoid mixing design, coding, and testing.

✔ Lead Architect Insight

I learned that AI is powerful, but I must evaluate and guide it to maintain a clean and scalable system.