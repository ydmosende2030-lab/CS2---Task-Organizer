Core Implementation

The app uses a List of Dictionaries. Each task is a "packet" of information containing a string (name of task), a date object (deadline of the task), and a boolean (status of the task).

Technologies & Justification

Python - Used because it handles dates easily without extra software.
Time Module - Added to prevent the "Killed" error. By adding a 0.1-second pause when no input is detected, the CPU stays cool and the OS doesn't force the program to stop.

Design Decisions

Volatile Memory - Tasks are stored in RAM. This means the app is very fast and doesn't need "save file" permissions, but data resets when the program is closed.
User-Friendly Indexing - The app lets users type "1" for the first item (instead of "0") to make it more natural for non-programmers.
