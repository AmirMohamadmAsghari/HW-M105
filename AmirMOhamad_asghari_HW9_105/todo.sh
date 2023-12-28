#!/bin/bash

TODO_DIR="$HOME/todo_files"
TODO_FILE="$TODO_DIR/todo.txt"
DONE_FILE="$TODO_DIR/done.txt"
DELETED_FILE="$TODO_DIR/deleted.txt"

# Create the directory and ToDo files if they don't exist
if [ ! -d "$TODO_DIR" ]; then
    mkdir "$TODO_DIR"
fi

for file in "$TODO_FILE" "$DONE_FILE" "$DELETED_FILE"; do
    if [ ! -e "$file" ]; then
        touch "$file"
    fi
done

# Function to add a new task
add_task() {
    echo "Adding a new task..."
    read -p "Enter the new task: " new_task
    echo "$new_task" >> "$TODO_FILE"
    echo "New task added: $new_task"
}

# Function to display uncompleted tasks
display_uncompleted_tasks() {
    echo "Uncompleted Tasks:"
    cat "$TODO_FILE"
}

# Function to mark an undone task as done
complete_task() {
    echo "Completing a task..."
    read -p "Enter the task to mark as completed: " task_to_complete
    sed -i "/$task_to_complete/d" "$TODO_FILE"
    echo "$task_to_complete" >> "$DONE_FILE"
    echo "Task completed: $task_to_complete"
}

# Function to display completed tasks
display_completed_tasks() {
    echo "Completed Tasks:"
    cat "$DONE_FILE"
}

# Function to delete a task
delete_task() {
    echo "Deleting a task..."
    read -p "Enter the task to delete: " task_to_delete
    sed -i "/$task_to_delete/d" "$TODO_FILE"
    sed -i "/$task_to_delete/d" "$DONE_FILE"
    echo "$task_to_delete" >> "$DELETED_FILE"
    echo "Task deleted: $task_to_delete"
}

# Function to display deleted tasks
display_deleted_tasks() {
    echo "Deleted Tasks:"
    cat "$DELETED_FILE"
}

# Function to search in all files
search_tasks() {
    echo "Searching in all files..."
    read -p "Enter the search term: " search_term
    grep -i "$search_term" "$TODO_FILE" "$DONE_FILE" "$DELETED_FILE"
}

# Menu options
PS3="Please select an option: "
options=("Add New Task" "Display Uncompleted Tasks" "Complete Task" "Display Completed Tasks" "Delete Task" "Display Deleted Tasks" "Search Tasks" "Exit")

# Main loop of the program
while true; do
    select opt in "${options[@]}"; do
        case $REPLY in
            1) add_task ;;
            2) display_uncompleted_tasks ;;
            3) complete_task ;;
            4) display_completed_tasks ;;
            5) delete_task ;;
            6) display_deleted_tasks ;;
            7) search_tasks ;;
            8) echo "Goodbye!"; exit ;;
            *) echo "Invalid option" ;;
        esac
        break
    done
done
