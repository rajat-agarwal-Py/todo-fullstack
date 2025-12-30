import TaskItem from "./TaskItem";

function TaskList({ tasks, onUpdate }) {
  return (
    <ul>
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onUpdate={onUpdate} />
      ))}
    </ul>
  );
}

export default TaskList;
