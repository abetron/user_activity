# Communication Contract
## How to REQUEST Data
### Start view_activity Server
Can be done two different ways.
1. In the Pycharm IDE run view_actiity.py by pressing the green arrow to run (Shift + F10).
2. Type "python view_activity.py" in a terminal window.

### Connect to Server
Code needed on the client side

    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5558")

### Requesting the Data
The client by sending a user id in the form of a string.
An example call is as follows:

    socket.send_string("1")

There is input validation built-in on the microservice server side.
If the user id does not exist, the server will respond with "User not found".

    
## How to RECEIVE Data
Once the user activity microservice has responded, the client can receive the message with:

    message = socket.recv()
    message.decode()

message.decode() can be printed out to the terminal or assigned to a variable for later use. The response will be in the following format.

    User ID: 1
    Interactions: 0
    Images Viewed: Sunset

If there are no images viewed, the response will be similar to:

    User ID: 4
    Interactions: 0
    Images Viewed: No images recorded.

## UML Sequence Diagram

