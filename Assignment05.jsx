import { useState } from "react";
import "./App.css";

function App() {
const [todos, setTodos] = useState([]);
const [input, setInput] = useState("");

const addTodo = () => {
if (input.trim() === "") return;
setTodos([...todos, input]);
setInput("");
};

const deleteTodo = (index) => {
setTodos(todos.filter((_, i) => i !== index));
};

return (
<div className="container">
<div className="todo-card">
<h1> My Todo App</h1>

<div className="input-box">
<input
type="text"
placeholder="Enter your task..."
value={input}
onChange={(e) => setInput(e.target.value)}
/>
<button onClick={addTodo}>Add</button>

</div>

<div className="todo-list">
{todos.map((todo, index) => (
<div className="todo-item" key={index}>
<span>{todo}</span>
<button
className="delete"
onClick={() => deleteTodo(index)}
>

</button>
</div>
))}
</div>
</div>
</div>
);
}

export default App;