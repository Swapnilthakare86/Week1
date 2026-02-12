// Todo App (Console Based)
let todos = JSON.parse(localStorage.getItem("todos")) || [];

function saveTodos() {
  localStorage.setItem("todos", JSON.stringify(todos));
}

// Show Menu
function showMenu() {
  console.log("\n--- ToDo App ---");
  console.log("1. Add Todo");
  console.log("2. View Todos");
  console.log("3. Mark Todo Completed");
  console.log("4. Delete Todo");
}

let title,No;
     
   showMenu();
    
  
//add todos
function addTodo(title) {
  
  if (!title || title.trim() === "") {
    console.log("Title cannot be empty");
    return;
  }

  todos.push({ title, completed: false });
  saveTodos();
  console.log("Todo added successfully");
}

//view todos
function viewTodos() {
   if (!isAvailableTodo()) 
    {
        return;
    }
  const tableData = todos.map((todo, index) => ({
    No: index + 1,
    Title: todo.title,
    Status: todo.completed ? "Completed" : "Pending",
  }));

  console.table(tableData);
}

//markasComplete
function markCompleteTodo(No) {
 if (!isAvailableTodo()) 
    {
        return;
    }
  const index = Number(No) - 1;
  if (!isValidTodoNo(index))
    {
     return;
    }

  todos[index].completed = true;
  saveTodos();
  console.log("Todo marked as completed");
}

//Delete
function deleteTodo(No) {
  if (!isAvailableTodo()) 
    {
        return;
    }
  const index = Number(No) - 1;
  if (!isValidTodoNo(index))
    {
     return;
    }

  todos.splice(index, 1);
  saveTodos();
  console.log("Todo deleted");
}

//checking function
function isAvailableTodo() {
  if (todos.length === 0) {
    console.log("No Todos Available.");
    return false;
  }
  return true;
}

function isValidTodoNo(index) {
  if (isNaN(index) || index < 0 || index >= todos.length) {
    console.log("Invalid Todo number");
    return false;
  }
  return true;
}

