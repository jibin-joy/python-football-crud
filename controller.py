from db import connect_db
from tabulate import tabulate

#VIEW STYLE
def format_player(p):
    return f"ID: {p[0]} | Name: {p[1]} | Position: {p[2]} | Number: {p[3]}"

#VALIDATION
def validate_string(value, field_name):
    value = value.strip()

    if not value:
        print(f"❌ {field_name} cannot be empty")
        return None

    if not value.isalpha():
        print(f"❌ {field_name} must contain only letters")
        return None

    return value


def validate_number(value):
    try:
        return int(value)
    except ValueError:
        print("❌ Number must be integer")
        return None

# CREATE
def add_player():
    name = validate_string(input("Enter name: "), "Name")
    if not name:
        return

    position = validate_string(input("Enter position: "), "Position")
    if not position:
        return

    number = validate_number(input("Enter number: "))
    if number is None:
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO players (name, position, number) VALUES (?, ?, ?)",
        (name, position, number)
    )

    conn.commit()
    conn.close()

    print("✅ Player added successfully")


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
    player_id = validate_number(input("Enter player ID: "))
    if player_id is None:
        return

    name = validate_string(input("New name: "), "Name")
    if not name:
        return

    position = validate_string(input("New position: "), "Position")
    if not position:
        return

    number = validate_number(input("New number: "))
    if number is None:
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE id=?", (player_id,))
    if not cursor.fetchone():
        print("❌ Player not found")
        conn.close()
        return

    cursor.execute(
        "UPDATE players SET name=?, position=?, number=? WHERE id=?",
        (name, position, number, player_id)
    )

    conn.commit()
    conn.close()

    print("✅ Player updated successfully")


# DELETE
def delete_player():
    player_id = validate_number(input("Enter player ID: "))
    if player_id is None:
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE id=?", (player_id,))
    if not cursor.fetchone():
        print("❌ Player not found")
        conn.close()
        return

    cursor.execute("DELETE FROM players WHERE id=?", (player_id,))
    conn.commit()
    conn.close()

    print("✅ Player deleted successfully")

#SEARCH
def search_player():
    name = input("Enter name to search: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()

    if results:
        for p in results:
            print(format_player(p))
    else:
        print("❌ No player found")

    conn.close()