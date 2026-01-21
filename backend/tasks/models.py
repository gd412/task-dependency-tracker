from django.core.exceptions import ValidationError
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('blocked', 'Blocked'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskDependency(models.Model):
    task = models.ForeignKey(Task, related_name='main_task', on_delete=models.CASCADE)
    depends_on = models.ForeignKey(Task, related_name='depends_on', on_delete=models.CASCADE)

    def clean(self):
        """
        Prevent circular dependencies.
        """
        if self.task == self.depends_on:
            raise ValidationError("A task cannot depend on itself!")

        # Check for indirect circular dependency
        def has_cycle(current_task, target_task):
            """Recursively check dependencies"""
            for dep in current_task.main_task.all():
                if dep.depends_on == target_task:
                    return True
                if has_cycle(dep.depends_on, target_task):
                    return True
            return False

        if has_cycle(self.depends_on, self.task):
            raise ValidationError(f"Circular dependency detected: '{self.task}' cannot depend on '{self.depends_on}'.")

    def save(self, *args, **kwargs):
        self.clean()  # run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.task.title} depends on {self.depends_on.title}"
