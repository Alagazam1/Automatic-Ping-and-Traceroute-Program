# Automatic-Ping-and-Traceroute-Program

First attempt of an automatic ping and traceroute/tracert program

You can access the program by downloading the .exe file; "Automatic Ping and Traceroute Program.exe"

The full code for the program can be found in the file: "ping_traceroute_final_program.py"

This program attempts to:

  1) Automatically perform 3 ping commands via the Window's command prompt 
  2) Automatically perform a traceroute command via the Window's command prompt
  3) Automatically perform both the 3 ping commands and the traceroutet command via the Window's command prompt
  4) Perform options 1-3 but with manual/user-defined input

and then output the results in a text file; "ping_traceroute_results.txt", which will then be opened to display the results to the user.

--------------------------------------------------------------------------
Note; 

- The 3 IP addresses for the ping tests are:

   1) The loopback address of the user's computer; 127.0.0.1
   2) The default gateway of the users' network
   3) A public Google DNS server address; 8.8.8.8
 
- The ping command is set to "-n 15"; it pings the target IP address 15 times
- The IP address used for the tracert test is a public Google's DNS Server Address(8.8.8.8) 
- "-d" has been added to the automatic traceroute command; To not resolve ip addresses to hostnames.

- If any errors occur during the program's execution, the program will log this in a text file; "ping_traceroute_error_log.txt"
- The text files; "ping_traceroute_results.txt" and "ping_traceroute_error_log.txt" will be located in the same directory/folder that the "Automatic Ping and Traceroute Program.exe" is in.

Program Limitations:

- User will need notepad.exe on their PC.
- Program currently only works on the Window OS.
- For the ping command, IPv6 addresses and networks may not work.
