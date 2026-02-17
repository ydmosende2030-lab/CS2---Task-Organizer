Updated Feature List

Task Management - This allows the users create/add tasks with its deadlines
Status Tracking - This allows the users to view their tasks if they are completed or not so they are able to mark it done once it is finished.
Urgency Status - This allows users to view urgent tasks as it comes with how many days you have left to do it, enabling them to do it immediately.
Data/Task Removal - This allows the users to remove task entries from the list.

Revised Function Structure

add_task() - Handles input and datetime conversion.
view_tasks() - Iterates through the global tasks list.
mark_done() - Modifies the completed key in a specific dictionary.
show_urgent() - Performs date arithmetic to find upcoming deadlines of tasks.
delete_task() - Uses .pop90 to remove data from the list.
while true - The primary control loop for the interface.
