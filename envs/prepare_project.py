"""
This Python file runs a script that creates a Brightway2 project called 'winter-school'
and imports the ecoinvent 3.10 cutoff database
"""

import sys
import bw2data as bd
import bw2io as bi

# Create a new project
bd.projects.set_current("winter-school")

def import_ecoinvent(username, password):
    if "ecoinvent-3.10-cutoff" not in bd.databases:
        bi.import_ecoinvent_release(
            version="3.10",
            system_model="cutoff",  # other options are "consequential", "apos" and "EN15804"
            username=username,
            password=password,
            biosphere_name="biosphere"  # optional, otherwise a name is chosen for you
        )
        print("Import completed successfully!")
    else:
        print("Database 'ecoinvent 3.10 cutoff' already exists")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python prepare_project.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    print(f"Importing ecoinvent 3.10 with username: {username}")
    import_ecoinvent(username, password)
    print(f"List of databases in {bd.projects.current} project: {bd.databases}")
