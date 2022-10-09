from practikum import func

print('Справку по командам можно вызвать через ENTER или командой help')
while True:
    command = input('Введите команду: ')
    command = command.split(' ')
    if command[0] == 'exit':
        break

    elif command[0] == 'help' or command[0] == '':
        func.help()

    elif command[0] == 'create_folder':
        func.create_folder(command[1])

    elif command[0] == 'del_folder':
        func.del_folder(command[1])

    elif command[0] == 'change_dir_up':
        func.change_dir_up()

    elif command[0] == 'change_dir':
        write_dir = input("Введите имя папки: ")
        func.change_dir(write_dir)

    elif command[0] == 'make_file':
        func.make_file(command[1])

    elif command[0] == 'write_file':
        write_text = input("Введите текст: ")
        func.write_file(command[1], write_text)

    elif command[0] == 'read_file':
        func.read_file(command[1])

    elif command[0] == 'del_file':
        func.del_file(command[1])

    elif command[0] == 'copy_file':
        func.copy_file(command[1], command[2])

    elif command[0] == 'move_file':
        func.move_file(command[1], command[2])

    elif command[0] == 'rename_file':
        func.rename_file(command[1], command[2])

    else:
        print('Ошибка, вызовите help')