students = []

def student_app():
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add | 2. View | 3. Update | 4. Delete | 5. Search | 6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            students.append({"id": sid, "name": name})
            print("Added successfully!")
        
        elif choice == '2':
            for s in students:
                print(f"ID: {s['id']} | Name: {s['name']}")
        
        elif choice == '3':
            target_id = input("Enter ID to update: ")
            for s in students:
                if s['id'] == target_id:
                    s['name'] = input("Enter new name: ")
                    print("Updated!")
                    break
        
        elif choice == '4':
            target_id = input("Enter ID to delete: ")
            students[:] = [s for s in students if s['id'] != target_id]
            print("Deleted if found.")
        
        elif choice == '5':
            query = input("Search by Name or ID: ")
            found = [s for s in students if query.lower() in s['name'].lower() or query == s['id']]
            print("Results:", found)
        
        elif choice == '6':
            break

# To run the app, call: student_app()