
from priority_queue import Task, PriorityQueue


def run_scheduler(tasks):
    """
    Simulate non-preemptive priority scheduling.

    Each task requires one time unit.
    Higher numerical priority is processed first.
    """

    queue = PriorityQueue()
    current_time = 0
    completed = []
    missed_deadlines = 0

    tasks = sorted(tasks, key=lambda task: task.arrival_time)
    next_task = 0

    print("TASK SCHEDULER SIMULATION")
    print("-" * 65)

    while next_task < len(tasks) or not queue.is_empty():

        # Add tasks that have arrived.
        while (
            next_task < len(tasks)
            and tasks[next_task].arrival_time <= current_time
        ):
            task = tasks[next_task]
            queue.insert(task)

            print(
                f"Time {current_time}: "
                f"Task {task.task_id} arrived "
                f"(Priority {task.priority})"
            )
            next_task += 1

        if queue.is_empty():
            current_time = tasks[next_task].arrival_time
            continue

        # Execute the highest-priority task.
        task = queue.extract_max()
        start_time = current_time
        current_time += 1

        waiting_time = start_time - task.arrival_time
        turnaround_time = current_time - task.arrival_time

        deadline_met = current_time <= task.deadline

        if not deadline_met:
            missed_deadlines += 1

        completed.append({
            "task_id": task.task_id,
            "priority": task.priority,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time,
            "deadline_met": deadline_met
        })

        print(
            f"Time {start_time}-{current_time}: "
            f"Task {task.task_id} completed | "
            f"Priority: {task.priority} | "
            f"Wait: {waiting_time} | "
            f"Deadline met: {deadline_met}"
        )

    print("\nSCHEDULING RESULTS")
    print("-" * 65)

    total = len(completed)

    if total == 0:
        print("No tasks to schedule.")
        return completed

    avg_waiting = sum(
        task["waiting_time"] for task in completed
    ) / total

    avg_turnaround = sum(
        task["turnaround_time"] for task in completed
    ) / total

    print(f"Total tasks completed: {total}")
    print(f"Average waiting time: {avg_waiting:.2f}")
    print(f"Average turnaround time: {avg_turnaround:.2f}")
    print(f"Missed deadlines: {missed_deadlines}")
    print(
        f"Deadline success rate: {(total - missed_deadlines)/total*100:.1f}%")

    return completed


if __name__ == "__main__":
    tasks = [
        Task(1, 3, 0, 4),
        Task(2, 5, 0, 2),
        Task(3, 2, 1, 6),
        Task(4, 4, 2, 4),
        Task(5, 1, 3, 7),
        Task(6, 6, 3, 5),
        Task(7, 2, 4, 8),
        Task(8, 5, 5, 7)
    ]

    run_scheduler(tasks)
