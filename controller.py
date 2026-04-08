from db import connect_db
from tabulate import tabulate

# CREATE
def add_player():
    name = input("Enter name: ").strip()

    if not name:
        print("❌ Name cannot be empty")
        return

    position = input("Enter position: ").strip()

    if not position:
        print("❌ Position cannot be empty")
        return

    try:
        number = int(input("Enter number: "))
    except:
        print("❌ Number must be integer")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO players (name, position, number) VALUES (?, ?, ?)",
        (name, position, number)
    )

    conn.commit()
    conn.close()

    print("✅ Player added")


# READ

def view_players():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()

    if players:
        print(tabulate(players, headers=["ID", "Name", "Position", "Number"], tablefmt="grid"))
    else:
        print("No players found")

    conn.close()


# UPDATE
def update_player():
    player_id = int(input("Enter ID: "))
    name = input("New name: ")
    position = input("New position: ")
    number = int(input("New number: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE players SET name=?, position=?, number=? WHERE id=?",
        (name, position, number, player_id)
    )

    conn.commit()
    conn.close()

    print("✅ Updated")


# DELETE
def delete_player():
    player_id = int(input("Enter ID: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM players WHERE id=?", (player_id,))

    conn.commit()
    conn.close()

    print("✅ Deleted")

def search_player():
    name = input("Enter name to search: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()

    if results:
        for p in results:
            print(p)
    else:
        print("❌ No player found")

    conn.close()