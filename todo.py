# A simple todo list manager command line interface (CLI).You can add, list, complete, and remove tasks using  CLI.

import click  
import json
import os 

# File to store the todo list tasks
TODO_FILE ="todo.json"

def load_task():
    # Load tasks from the TODO_FILE.           
    # If the file doesn't exist, return an empty list.
    if not os.path.exists(TODO_FILE):
        return[]    # No tasks saved yet, returning empty list
    with open(TODO_FILE,"r") as file:
        return json.load(file)
    
def save_task(tasks):
# Save the tasks list to the TODO_FILE in JSON format.
    with open(TODO_FILE,'w') as file:
        json.dump(tasks,file,indent=4)

@click.group()
def cli():
   """ simple todo list manager  """
   pass

@click.command()
@click.argument("task")
def add(task):
    """ add a new task to the list"""
    tasks = load_task()
    tasks.append({"task":task , "done": False})
    save_task(tasks)
    click.echo(f"Task added successfully! ✅📋: {task}")

@click.command()
def list():
    """list all the tasks"""
    tasks = load_task()
    if not tasks: 
        click.echo("No task found: {task_number} 🔍❌")
        return
    for index, task in enumerate(tasks,1):
        status = "✅" if task["done"] else "❌" 
        click.echo(f"{index}.{task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """mark a task as compelted"""
    tasks = load_task()
     # Check if the task number is valid
    if 0 < task_number <= len(tasks):
         tasks[task_number - 1]["done"] = True
         save_task(tasks)
         click.echo(f"Task {task_number} marked as completed ✅✔️")
    else:
        click.echo(f"Invalid task number: {task_number} ❌") 
@click.command()
@click.argument("task_number",type=int)
# remove the task from the list using index number
def remove(task_number):
    """remove task from the list"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
       remove_task = tasks.pop(task_number -1)
       save_task(tasks)
       click.echo(f"Removed task successfully: {remove_task['task']} ✔️🚮")
    else:
        click.echo("Invalid task number: {task_number} ❗🚫")

# Add the individual commands to the main CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == '__main__':
       # Run the CLI
    cli()

