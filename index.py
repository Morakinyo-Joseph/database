import json

try:
    # if json file exists
    with open('database.json') as f:
        data = json.load(f)

        info = data["mydata"]

        # input bio data
        last_name = input("Surname: ")
        first_name = input("Firstname: ")
        email = input("Email: ")

        while True:
            pass1 = input("Password: ")
            pass2 = input("Confirm Password: ")

            if pass1 == pass2:
                auto_id = len(info) + 1

                data2 = {
                    "id": auto_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "password": pass1,
                }
                info.append(data2)
                break
            else:
                print("Passwords do not match")

        with open('database.json', 'w') as f:
            json.dump(data, f, indent=2)

except FileNotFoundError:  # json file not found
    database = []

    # input bio data
    last_name = input("Surname: ")
    first_name = input("Firstname: ")
    email = input("Email: ")

    while True:
        pass1 = input("Password: ")
        pass2 = input("Confirm Password: ")

        if pass1 == pass2:
            auto_id = len(database) + 1
            data = {
                "id": auto_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": pass1,
            }
            database.append(data)
            break
        else:
            print("Passwords do not match")

    result = {
        "mydata": database
    }

    with open('database.json', 'w') as f:
        json.dump(result, f, indent=2)
