import features as ft
from time import sleep

my_tasks = []
tasks_rmd = []

while True:
    opt = ft.option_menu()
    if opt == '1':
        ft.insert_task(my_tasks)
    elif opt == '2':
        ft.tasks_list(my_tasks)
    elif opt == '3':
        ft.undo_action(my_tasks, tasks_rmd)
    elif opt == '4':
        ft.redo_action(my_tasks, tasks_rmd)
    elif opt == '5':
        ft.remove_task(my_tasks)
    elif opt == '6':
        print('Logout', end=' ')
        for i in range(3):
            print('*', end=' ')
            sleep(0.5)
        break


