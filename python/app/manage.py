import sys

from commands import migrate
from commands import status
from commands import reset


COMMANDS = {

    "migrate": migrate.run,

    "status": status.run,

    "reset": reset.run,

}


def main():

    if len(sys.argv) < 2:

        print("""

Uso:

python manage.py migrate

python manage.py status

python manage.py reset

        """)

        return

    command = sys.argv[1]

    func = COMMANDS.get(command)

    if not func:

        print("Comando inexistente.")

        return

    func()


if __name__ == "__main__":
    main()