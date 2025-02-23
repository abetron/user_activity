import json
import zmq
import time


# ZeroMQ Setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")
print("User activity server running")
# Listening for requests

while True:
    # Added to the while loop to access latest version of users.json
    with open('users.json') as users_file:
        users = json.load(users_file)

    message = socket.recv()
    print(f"Received request from client: {message.decode()}")

    if len(message) > 0:
        if message.decode() == 'Q':
            break
        else:
            user_id = message.decode()

            # Checks to see if user id is valid.
            if user_id in users:
                interactions = users[user_id]['interactions']
                images_viewed = users[user_id]['images_viewed']

                response = f"User ID: {user_id}\n" + f"Interactions: {interactions}\n"

                if images_viewed:
                    response += f"Images Viewed: {', '.join(images_viewed)}"
                else:
                    response += "Images Viewed: No images recorded."

                socket.send_string(response)

            else:
                socket.send_string("User not found.")

    time.sleep(1)

context.destroy()
