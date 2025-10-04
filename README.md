# Project Flash

## Overview

This is some work for my 2025 NCEA Level 3 Digitech Class at [Wainuiomata High School](https://wainuiomatahigh.school.nz/).

## Potential Names

- [x] Kādo *('Card' Japanese Literal Translation.)*
- [ ] MemMori *(MEM, half mental with m. Mori, half memory with i.)*

## Planning Steps

- [x] 1. Make Name
- [x] 2. Write Project Brief
- [x] 3. Make Logo

- [x] Document Logo Process

## Project Brief

This app will be a flashcard app to assist with learning using a spaced repetitional algorithm. I will keep it in the command-line using python. It will give the user small motivational prompts to keep them engaged, and it will retain all it's data through an external file, allowing for modularity and portability.

## Leitner System

The Leitner System for spaced repetition is a system of priority management that adjusts to your individual recollection of each card. Put simply, the better you know one card, the less you need to revise it, and that time gap between the revision will adjust your mind to recalling that piece of information at random times, further enhancing your knowledge. Duolingo uses much the same system (albeit with their own fancy language), and their documentation is here: [duo docs](https://blog.duolingo.com/how-we-learn-how-you-learn)

![LeitnerSystem](https://examstudyexpert.com/wp-content/uploads/2022/10/The-Leitner-System.jpg)

## Leitner System Implementation - Spaced Repetition Basic Diagram

This diagram shows how I will implement the Leitner system in my program.

![LeitnerSystem](leitnerSystemDiagram/LeitnerSystem.drawio.svg)

# Project Kādo

![KadoLogo](Logo/Kado-v2(1600x1600).png)

## Requirements

- [x] Text-Based Interface
- [x] Template CSV for User Simplicity
- [x] Simple Terms/Function
- [x] Save to External File (Including User Data)
- [x] Spaced Repetition Algorithm (Basic)
- [x] User Retention Methods (Affirmation, Progress Tracking, etc.)

### Stakeholder Feedback

- Kaedyn (post-coreFlowchart)
    - [x] Add emojis for clarity
- Father (post-prototype)
    - [x] Have summary of study at end
    - [x] Make randomness algorithm (Spaced Repetition)

### Trialling

- Leitner System (2025.09.15)
    - Should the system be based on time taken to answer or number of times the card has been revised?
    - Both integrated would be ideal, though an algorithmic nightmare, a potential future addition.
    - Time taken factors: 
        - Prior knowledge included in factor
        - Follows leitner system
    - Number of time factors:
        - Prior knowledge not included
        - Simpler for computation
    - Final verdict: Utilise Time Taken for leitner system and prior knowledge
- Further trialling was done in word document for stakeholder feedback input, periodic pastes shall be conducted when possible.
- CSV Template Usability Trial (2025.09.28)
    - I trialled the template CSV by giving two of my friends (Darrin, Kaedyn) a random task to add 5 flashcards to the template csv.
    - Feedback: 
        - Leitner Box Column Barriers Unknown (1-5, user should start with all at 1 but not shown in documentation)
        - How to add commas in csv?
    - Implementation:
        - Added two more lines of template with examples and description.
- Leitner System Refinement Trial (2025.09.29)
    - I gave my father and Darrin each two versions to try, one with a shorter time interval between leitner values, and one with the current values. 
    - Feedback:
        - Shorter was better, even with little known knowledge they reached values 4-5
    - Implementation
        - Shortened leitner times. Adjusted program and program tests to reflect modifications
- Tutorial Timing Refinement Trial (2025.10.02)
    - I showed my friend Caleb the tutorial, and he suggested the text have a time delay to not bombard the user with imformation at a rapid rate. I agreed, and presenting my program live to Caleb and another friend (Samantha), I gradually refined the time value.
    - Trial Process
        - We started at 1 second time lag before each text line, but they felt that was too much.
        - We then switched to having an around 4-second delay for the two paragraphs, and this went over well with them, though it wasn't enough time for them to read.
        - A delay of 7-seconds each paragraph was settled upon.

## Programming Primary Steps

- [x] 1. Simply & Quantify Spaced Repetition Algorithm - Leitner System
- [x] 2. Flowchart Program Process (Solution Design)
    - Keep Terminology/Program Function Simple
- [x] 3. Make Example of Working Program w/o Code (text flowchart w/ examples)
- [x] 4. Make Program.

## Flowchart

Documentation for the Program Flowchart [is here](programDiagram/)

## Testing

Documentation for automated and manual testing is available at [the tests folder.](tests/)

# Planning

I utilised Microsoft Planner to plan out my project, and am currently using it as a central list of requirements and necessities.\
Here is how it looks as of this commit:\
![2025.09.27Planner](planning/Screenshot%202025-09-27%20004339.png)

# Relevant Implications

1. I have utilised error-catching algorithms throughout the program to increase it's usability. This is an important aspect to include because if I am to create a smooth experience for the end-user, it is best practise to assume any and all accidental mishaps will occur with the program. If the user enters a value which triggers any exception, it shouldn't break the program and cause it to cease function; i.e. crash. It should run ahead and simply ask the user to repeat themselves. As an example, in [actions.py](actions.py) for when the user is asked whether or not they've gotten the question's answer correct, the program creates a `while` loop which is dependent on the user entering a valid value, so the user is effectively forced into picking a value that truly matches their intent. Put simply it will keep asking the user for input until they enter `y` or `n`.

2. My program is designed and built with future-proofing in mind. The primary method through which I have done this is by making my program with Object-Oriented Programming. This philosophy, in contrast to a monolithic or linear design approach, allows for modular additions/upgrades while the core of the system remains intact. `fileManagement` in [data.py](data.py) handles managing the external CSV file, `cardParse` in [actions.py](actions.py) manages loading and saving flashcards to and from the program memory, `studyTime` in [actions.py](actions.py) handles controlling the logic of the study session itself, and manages promoting cards from Leitner Box values. Finally, [main.py](main.py) runs the program in a loop until it is broken. The modularity of an Object-Oriented Programming can allow for simplicity in upgrades and fixes, as an example, if I wanted to add a module to allow an external API to modify the local cards, all I would need to do is create and define a function in a new class that I would put into [data.py](data.py), get it to bring in the API, and allow it to modify the file however it wants, to which then it would simply need to be referenced within [actions.py](actions.py). The modularity and systemic flow is of utmost importance for introducing elements to the program.