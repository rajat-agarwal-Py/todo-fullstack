import { useEffect, useState } from "react";
import api from "./api";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

function App() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    const res = await api.get("/tasks");
    setTasks(res.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <h2>ToDo App</h2>
      <TaskForm onTaskAdded={fetchTasks} />
      <TaskList tasks={tasks} onUpdate={fetchTasks} />
    </div>
  );
}

export default App;
