import api from "../api";

function TaskItem({ task, onUpdate }) {
  const toggleStatus = async () => {
    await api.put(`/tasks/${task.id}`, {
      status: task.status === "pending" ? "completed" : "pending",
    });
    onUpdate();
  };

  const deleteTask = async () => {
    await api.delete(`/tasks/${task.id}`);
    onUpdate();
  };

  return (
    <li>
      <span>
        {task.title} ({task.status})
      </span>
      <button onClick={toggleStatus}>✔</button>
      <button onClick={deleteTask}>❌</button>
    </li>
  );
}

export default TaskItem;
