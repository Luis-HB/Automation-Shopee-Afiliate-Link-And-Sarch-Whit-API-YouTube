import sys

from commands import migrate
from commands import status
from commands import reset
from commands import rollback
from commands import seed


COMMANDS = {

    "migrate": migrate.run,

    "status": status.run,

    "reset": reset.run,

    "rollback": rollback.run,

    "seed": seed.run,

}


def main():

    if len(sys.argv) < 2:

        print("""

Uso:

python manage.py migrate

python manage.py status

python manage.py reset

python manage.py rollback

python manage.py seed

        """)

        return

    command = sys.argv[1]

    func = COMMANDS.get(command)

    if func is None:

        print(f"Comando '{command}' inexistente.")

        return

    func()


if __name__ == "__main__":
    main()