import time
import datetime
import os


def file_check():
	if not os.path.exists("todo_list.txt"):
		file = open("todo_list.txt", "w")
		file.close()


def read_todos(path="todo_list.txt"):
	""" Reads the to do list file. """
	todo = []
	file_check()
	with open(path, "r") as file:
		todo = file.readlines()
	for index, element in enumerate(todo):
		if element == "\n":
			del todo[index]
	return todo


def write_todos(todo, path="todo_list.txt"):
	""" Writes to the to do list file. The function overwrites the item originally stored in the file. """
	with open(path, "w") as file:
		for task in todo:
			if task != "\n":
				file.write(task)
		print("Done!")


def show(todo):
	""" Shows the current to do list. """
	if len(todo) > 0:
		for index, element in enumerate(todo):
			print(f"{index + 1}. {element}")
	else:
		print("No items to show!")


def up(todo, item):
	index = todo.index(item)
	temp = todo[index - 1 if index - 1 > 0 else 0]
	todo[index] = temp
	todo[index - 1 if index - 1 > 0 else 0] = item
	return todo


def down(todo, item):
	index = todo.index(item)
	temp = todo[index + 1 if index + 1 < len(todo) else len(todo) - 1]
	todo[index] = temp
	todo[index + 1 if index + 1 < len(todo) else len(todo) - 1] = item
	return todo


def replace(todo, replace_item, replace_with):
	for index, value in enumerate(todo):
		if value == replace_item:
			todo[index] = replace_with
			return todo


def add(todo, item):
	""" Adds an item/task to the list. """
	if item.casefold() == "cancel":
		return todo
	todo.append(item)
	return todo


def delete(todo):
	""" Deletes a task from the to do list. """
	show(todo)
	item = input("Please enter item number to delete: ")
	try:
		del todo[int(item) - 1]
	except ValueError:
		print("Invalid value given")
		exit(1)
	return todo


def time_stamp():
	time_zone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
	return time.strftime(f"%A, %B %d, %Y @ %H:%M:%S {time_zone}")
