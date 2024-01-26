# python-project6
Snail Race Python Script
Introduction
This Python script simulates a simple text-based snail race game. Players can create snails with unique initials, and these snails compete in a race. The script uses the time.sleep() function to introduce delays, creating a dynamic race visualization in the console.

Features
Text-based snail racing simulation.
Customizable number of snails in each race.
Each snail has unique initials and random speed.
Visual representation of snail positions during the race.
Identification of the winning snail.
Requirements
Python 3.x
Installation
No additional libraries are required to run this script. It uses standard Python libraries time and random.

Usage
Run the script in a Python environment. Follow the on-screen prompts to set up the race:

Enter the number of snails participating in the race.
Assign two-character initials to each snail.
Start the race by pressing Enter.
Watch the progress of the snails in real-time.
The winner is announced at the end of the race.
Option to replay the game after each race.
Code Structure
class Snail: Defines the snail with attributes for name, speed, position, and animation frames.
getSnailList(): Function to create a list of snails for the race.
runRace(snaillist): Function to simulate the race. It uses time.sleep() to create a dynamic update of snail positions.
main(): Main function to initiate the game and handle replay functionality.
