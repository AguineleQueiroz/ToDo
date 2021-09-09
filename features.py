
def title_task(title):
    print('-' * 42)
    print(title.center(42))
    print('-' * 42)


def option_menu():
    title_task('OPTIONS')
    print(
        """        [1] - Insert Tasks
        [2] - List Tasks
        [3] - Undo Action
        [4] - Redo Action
        [5] - Remove a task
        [6] - Exit """
    )
    print('-' * 42)
    while True:
        opt = input('Action: ')
        if not opt.isdigit():
            print('\033[31mError: Invalid action code.\033[0;0m')
            continue
        break
    return opt


def insert_task(to_do_list):
    title_task('INSERT TASKS')
    while True:
        task = input('Add task: ')
        to_do_list.append(task)

        op = input('Continue? [y/n] ')
        if op.lower() != 'y':
            break


def tasks_list(to_do_list):
    title_task('TASKS LIST')
    if not to_do_list:
        print('\033[33mEmpty to-do list!\033[0;0m')
    else:
        for index, task in enumerate(to_do_list):
            print(index + 1, ' - ', task)


def undo_action(to_do_list, tasks_removed):
    title_task('UNDOING ACTION')
    if not to_do_list:
        print('\033[33mNothing to undo!\033[0;0m')
    else:
        last_task_added = to_do_list.pop()
        tasks_removed.append(last_task_added)
        print('Done!')


def redo_action(to_do_list, tasks_removed):
    title_task('REMAKING ACTION')
    if not tasks_removed:
        print('\033[33mNothing to redo!\033[0;0m')
    else:
        last_task_removed = tasks_removed.pop()
        to_do_list.append(last_task_removed)
        print('Done!')


def remove_task(to_do_list):
    title_task('REMOVE TASKS')
    print('\033[31mAttention! This action cannot be reversed!\033[0;0m')
    while True:
        cod_task = input('\nNumber of the task: ')
        if not cod_task.isdigit():
            print('\033[31mError: Invalid task number.\033[0;0m')
            continue
        break
    for index, tasks in enumerate(to_do_list):
        if index + 1 == int(cod_task):
            to_do_list.pop(to_do_list.index(tasks))
    print('Done!')
