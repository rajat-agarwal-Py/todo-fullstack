import { useState } from "react";
import api from "../api";

function TaskForm({ onTaskAdded }) {
  const [title, setTitle] = useState("");

  const submitHandler = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;

    await api.post("/tasks", { title });
    setTitle("");
    onTaskAdded();
  };

  return (
    <form onSubmit={submitHandler}>
      <input
        placeholder="New task"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button>Add</button>
    </form>
  );
}

export default TaskForm;
