from django.test import TestCase
from django.urls import reverse
from .models import Task, Tag


class TaskListViewTests(TestCase):
    """Tests for the task list page."""

    def setUp(self):
        self.tag = Tag.objects.create(name="work")
        self.task_done = Task.objects.create(
            content="Clean windows",
            is_done=True,
        )
        self.task_not_done = Task.objects.create(
            content="Buy 3 carrots",
            is_done=False,
        )
        self.task_done.tags.add(self.tag)

    def test_task_list_page_loads(self):
        """Ensure the home page returns 200."""
        response = self.client.get(reverse("tasks:task-list"))
        self.assertEqual(response.status_code, 200)

    def test_task_list_shows_all_tasks(self):
        """Ensure both tasks appear in the task list."""
        response = self.client.get(reverse("tasks:task-list"))
        task_list = response.context["task_list"]
        self.assertIn(self.task_done, task_list)
        self.assertIn(self.task_not_done, task_list)

    def test_task_ordering_not_done_first(self):
        """Ensure not-done tasks appear before done tasks."""
        response = self.client.get(reverse("tasks:task-list"))
        task_list = list(response.context["task_list"])
        not_done_index = task_list.index(self.task_not_done)
        done_index = task_list.index(self.task_done)
        self.assertLess(not_done_index, done_index)


class ToggleTaskTests(TestCase):
    """Tests for the toggle done/undo functionality."""

    def setUp(self):
        self.task = Task.objects.create(content="Complete project", is_done=False)

    def test_toggle_marks_task_as_done(self):
        """Toggling a not-done task should mark it as done."""
        self.client.get(reverse("tasks:task-toggle", kwargs={"pk": self.task.pk}))
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

    def test_toggle_marks_task_as_not_done(self):
        """Toggling a done task should mark it as not done."""
        self.task.is_done = True
        self.task.save()
        self.client.get(reverse("tasks:task-toggle", kwargs={"pk": self.task.pk}))
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_done)

    def test_toggle_redirects_to_task_list(self):
        """Toggle should redirect back to the task list."""
        response = self.client.get(
            reverse("tasks:task-toggle", kwargs={"pk": self.task.pk})
        )
        self.assertRedirects(response, reverse("tasks:task-list"))


class TagViewTests(TestCase):
    """Tests for tag list and CRUD pages."""

    def setUp(self):
        self.tag = Tag.objects.create(name="home")

    def test_tag_list_page_loads(self):
        """Ensure the tag list page returns 200."""
        response = self.client.get(reverse("tasks:tag-list"))
        self.assertEqual(response.status_code, 200)

    def test_tag_list_shows_tag(self):
        """Ensure created tag appears in the list."""
        response = self.client.get(reverse("tasks:tag-list"))
        self.assertIn(self.tag, response.context["tag_list"])

    def test_tag_create(self):
        """Ensure a new tag can be created via POST."""
        self.client.post(reverse("tasks:tag-create"), {"name": "shop"})
        self.assertTrue(Tag.objects.filter(name="shop").exists())

    def test_tag_delete(self):
        """Ensure a tag can be deleted."""
        self.client.post(
            reverse("tasks:tag-delete", kwargs={"pk": self.tag.pk})
        )
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())


class TaskCRUDTests(TestCase):
    """Tests for task creation and deletion."""

    def test_task_create(self):
        """Ensure a new task can be created via POST."""
        self.client.post(reverse("tasks:task-create"), {"content": "Buy milk"})
        self.assertTrue(Task.objects.filter(content="Buy milk").exists())

    def test_task_delete(self):
        """Ensure a task can be deleted."""
        task = Task.objects.create(content="Task to delete")
        self.client.post(
            reverse("tasks:task-delete", kwargs={"pk": task.pk})
        )
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
