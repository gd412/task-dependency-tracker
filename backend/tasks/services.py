def update_task_status(task):
    deps = task.dependencies.all()

    if not deps.exists():
        return

    statuses = [d.depends_on.status for d in deps]

    if any(s == 'blocked' for s in statuses):
        task.status = 'blocked'
    elif all(s == 'completed' for s in statuses):
        task.status = 'in_progress'
    else:
        task.status = 'pending'

    task.save()
