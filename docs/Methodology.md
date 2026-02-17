Core Implementation

- The app uses a List of Dictionaries. Each task is a "packet" of information containing a string 
(name of task), a date object (deadline of the task), and a boolean (status of the task).

Technologies & Justification

- Python: Used because it handles dates easily without extra software.
    
- Time Module: Added to prevent the "Killed" error. By adding a 0.1-second pause when no input 
is detected, the CPU stays cool and the OS doesn't force the program to stop.

Design Decisions

- Volatile Memory: Tasks are stored in RAM. This means the app is very fast and doesn't need 
"save file" permissions, but data resets when the program is closed.
    
- User-Friendly Indexing: The app lets users type "1" for the first item (instead of "0") to 
make it more natural for non-programmers.

Ethical Considerations in Programming Choices

- User Privacy: Information stored inside the program is only temporary and will not be recorded.

- Accessibility: The software can be accessed and used by a variety of people, mostly those who find
it difficult or troublesome to organize tasks by themselves.
