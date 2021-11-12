import sys
import item
import user
import order

if __name__ == "__main__":
    arguments = sys.argv

    section = arguments[1]
    command = arguments[2]
    params = arguments[3:]
    print(section, command, params)

    if section == "user":
        user.set_command_and_params(command, params)
    elif section == "item":
        item.set_command_and_params(command, params)
    elif section == "order":
        order.set_command_and_params(command, params)

