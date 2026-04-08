from player import create_table
from controller import add_player, view_players, update_player, delete_player

create_table()

while True:
    print("\n--- Football Manager ---")
    print("1. Add Player")
    print("2. View Players")
    print("3. Update Player")
    print("4. Delete Player")
    print("5. Search Player")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_player()
    elif choice == "2":
        view_players()
    elif choice == "3":
        update_player()
    elif choice == "4":
        delete_player()
    elif choice == "5":
        search_player()
    elif choice == "6":
        break
        print("Invalid choice")