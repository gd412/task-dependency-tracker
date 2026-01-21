from django.core.exceptions import ValidationError

def check_circular_dependency(task, depends_on):
    """
    Check if adding 'depends_on' to 'task' creates a cycle.
    Raises ValidationError if a circular dependency exists.
    """
    visited = set()

    def visit(t):
        if t.id in visited:
            return False
        visited.add(t.id)
        # Get tasks that t depends on
        dependencies = [d.depends_on for d in TaskDependency.objects.filter(task=t)]
        for dep in dependencies:
            if dep.id == task.id:  # Cycle detected
                return True
            if visit(dep):
                return True
        return False

    if visit(depends_on):
        raise ValidationError(f"Circular dependency detected: {task.title} ↔ {depends_on.title}")
