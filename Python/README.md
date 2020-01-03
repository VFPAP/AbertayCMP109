# Python Networking Applications Assessed Lab

During the first term of the first year, I've built two Python networking programs for an assignment of this module.
A client-server Calculator and a client-server Document Statistics.

## Details

* UDPCalc_client.py

  - Uses socket library to use sockets.
  - Asks user for the operation and does some client-side verification: operation must have one operator (+, -, *, /) or ‘exit’.
  - Sends operation to the server and prints the server’s response.
  - If the server’s response is ‘exit’ (in case the user had sent ‘exit’ as well), closes the connection exits the program.
 
* UDPCalc_server.py

  - Uses socket library to use sockets.
  - I defined a function parseDigits() that checks if the digits are valid and handles float digits like this:
  - It takes an argument: a list with both digits.
  - Checks that it’s receiving two digits.
  - If both digits are valid digits (without ‘.’), they’re both int.
  - Else, if both digits have a ‘.’ , they’re both floats.
  - Else, if only the one has ‘.’ , only that one is float and the other is int.
  - Else, at least one of them is not valid so returns an empty list.
  - Starts to listen for connections.
  - Receives operation and clears whitespaces.
  - If the operation contains ‘exit’, send ‘exit’ back to client, break out the loop and close connection.
  - Else, if contains only one of the operators (+, -, *, /) and parseDigits() returned a valid list, do the operation according to operator and send back the result to the client.
  - Else, there’s something wrong with the operation received so throws error, and jumps back to the beginning of the loop.


* TCPStats_client.py

  - Uses socket library to use sockets.
  - Establishes the TCP connection with the server.
  - Asks for filename and tries to open it in read+binary mode so the file is ready to be sent.
  - Checks if filename ends with ‘.txt’.
  - If the user types ‘exit’ instead of the filename, the client sends ‘exit’ to the server and closes the connection.
  - If it receives the stats from the server, prints them.
  - Closes the connection and loops back to the beginning.

* TCPStats_server.py

  - Uses socket library to use sockets.
  - Starts to listen for connections.
  - Receives file.
  - If the file content is ‘exit’, breaks out of the loop and closes the connection.
  - If the file is a not empty string starts to work on it:
  - Initialises two variables with int ‘0’ to store the stats.
  - Divides the file into a list formed by each line of the file, removing carriage return characters.
  - Goes through every line and if it not empty, counts the number of characters and the number of words.
  - Creates a string containing the values of the variables that are storing the stats and sends it to the client.
  - Without closing the connection, loops to the beginning.
  - If for some reason the file received is not a string, ignores that and returns to the beginning of the loop.
  
## Author
**Vasco Pinto**
<br>Twitter: [@0xVFPAP](https://twitter.com/0xVFPAP)
<br>LinkedIn: [Vasco Pinto](https://linkedin.com/in/vascopinto97)
<br>OpenBugBounty: [VFPAP](https://www.openbugbounty.org/researchers/VFPAP)
