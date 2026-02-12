# XTS-Week1
This project is a console-based Todo application.

# Requirements
   - HTML
   - Javascript

 
# Project Features

The Todo App use Following Functions:

# showMenu()

# 1. Add Todo
   - Adds a new task to the todo list.
   - Implemented using the function:
        addTodo(title)

# 2. View Todos
    - Displays all todos in a tabular format in the console.
    - Implemented using:
        viewTodos()

# 3. Mark Todo as Complete
    - Marks a selected todo as completed.
    - Implemented using:
        markCompleteTodo(No)

# 4. Delete Todo
    - Removes a todo from the list.
    - Implemented using:
        deleteTodo(No)

# JavaScript Concepts Used
1. Variables- let is used to declare variables.

2. Arrays- Used to store the list of todos.
    Array methods used:

    push() → to add new todos
    splice() → to delete todos
    map() → to display and modify todos

3. Objects- Each todo is represented as an object:
{
  title: "Task name",
  completed: false
}
By default, every task is set as pending.

4. Functions- Functions are used to organize the logic.

    Arrow functions are used for cleaner and modern JavaScript syntax.

5. Console Methods

console.log() → to print messages
console.table() → to display todos in a table format

