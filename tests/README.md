# Testing the Program 

## With pytest:

To run test programs run `pytest -v` in your shell while the base directory is your working directory.

### [test_data.py](test_data.py)

This program first imports the data functions, then it utilizes `fileManagement.create_csv()` to first create a temp csv, then it uses `fileManagement.add_card()` to add a card to the csv. The test then verifies that the csv contains the added example card. It then removes the card using `fileManagement.remove_card()` and verifies that there is no card. Afterward it removes the temp csv to complete the process.

### [test_actions.py](test_actions.py)

This test module imports the `studyTime` class of [actions.py](actions.py) and then defines two dummy helpers (`dummyInput` & `dummyTime`) to spoof user input and user time taken respectively.\
The first test (`test_ask_card_leitner_timing`) first uses `monkeypatch` to spoof the existence of a csv using a test-defined dictionary, and creates a tuple to log expected end leitner value and required input. It asserts that the end leitner result for the card is as expected.\
The second test (`test_randomized_play_yields`) builds a spoof dictionary deck with expected states for primary (`1`-`3`) and secondary (`4`-`5`) leitner values. It simulates every card getting a quick answer and thus makes sure that each card was yielded only once.
The third test (`test_session_count`) builds a deck and then runs it with all answered, it then confirms that the `main()` function returns the correct number of cards that have been run: `3`.

### [test_main.py](test_main.py)

The primary testkit first imports the `main()` function, `cardParse` class, and test helpers. It then patches the `cardParse.load_cards()` to utilize a dictionary deck and effectively neuters the `cardParse.save_cards()` to prevent writing to disk. It also disables the `random.shuffle()` function so the values can be properly measured. It then mirrors the `dummyInput()` function from before to replicate user input, as well as the `dummyTime()` function to replicate user thought/consideration. The test runs the `main()` function and ensures the csv mutations are within expectations for the leitner values *(e.g. 8s → "5", 35s → "3")*.

## Test Descriptions

- Leitner System Timing Test
    - ID: `test_ask_card_leitner_timing`
    - This test verifies that `studyTime.ask_card()` correctly updates the Leitner box based on how long a user takes to answer and whether the answer is correct.
    - It simulates six scenarios with differing response times and accuracy, asserting the resulting Leitner box level.
- Card Priority/Randomizer Test
    - ID: `test_randomized_play_yields`
    - This test ensures that `studyTime.randomized_play()` yields all cards exactly once, prioritizing those in lower Leitner box values.
    - It simulates quick and accurate answers, and confirms that both primary and secondary cards are included.
- Adding/Removing Card Test
    - ID: `test_add_and_remove_card`
    - This test checks the `fileManagement` module by creating a temporary CSV, adding a card, asserting its presence, removing it, and confirming the deletion.
    - It ensures the add/remove functionality works as expected, and cleans up the temp file afterward.
- Program Flow Test
    - ID: `test_actions_main_runs`
    - This test validates the full `main()` function's flow, simulating card loading, saving, shuffling, user input, and timing.
    - It confirms that Leitner box values are updated correctly based on simulated user behavior (e.g., 8s → Box 5, 35s → Box 3).
- End Tally Test
    - ID: `test_session_count`
    - This test checks that `session_count` within main, correctly counts the session's card count. 
    - It confirms that the end value is 3 after simulating a user interaction. 
- Empty CSV Test
    - ID: `test_main_empty_csv`
    - This test confirms that the program redirects when confronted with a selection of an empty csv.
    - It makes sure that the program can add a card and detect when a csv is empty.
- File Selection Test
    - ID: `test_choose_existing_file`
    - This test confirms that the file selection menu selects the correct file upon user input.
    - It creates a false `cards` folder, with two files, selects the second file, then asserts that the file is correct after running the selection process.
- New File Creation Test
    - ID: `test_create_new_file`
    - This test simulates the user creating a new file with the selection menu dialog.
    - It very much just creates a file using the dialog.
- File Empty Folder Test
    - ID: `test_empty_folder `
    - This test makes sure that when the folder is empty and the user doesn't enter a value for the new card deck, that the end result is the creation of `new_cards.csv`.

## Testing
Tests can be simply run by installing and running `pytest -v` in Kādo program's root folder.\

iteration1 = Commit ID: [b19f1f1296ebb3e34016be64353b91a19a4026a2](https://github.com/YouthfulRicker2/Digitech2025-ProjectFlash/commit/b19f1f1296ebb3e34016be64353b91a19a4026a2)\
iteration2 = Commit ID: [98c131eae39c3d1e32b5677422061607361fd6e7](https://github.com/YouthfulRicker2/Digitech2025-ProjectFlash/commit/98c131eae39c3d1e32b5677422061607361fd6e7)\
iteration3 = Commit ID: [3630f9c40b8b4b470b15a0ece2e9d96e60739942](https://github.com/YouthfulRicker2/Digitech2025-ProjectFlash/commit/3630f9c40b8b4b470b15a0ece2e9d96e60739942)\
iteration4 = Commit ID: LATEST

N/A indicates that the feature wasn't implemented or tested in that iteration.

iteration1 was not tested due to the tests not being fully developed at that stage. They were developed alongside and completed slightly after iteration2.

| Test Friendly Name | Test ID | iteration1 | iteration2 | iteration3 | iteration4 |
|-------------------------------|-------------------------------|-------------|-------------|-------------|-------------|
| Leitner System Timing Test | `test_ask_card_leitner_timing` | N/A | Yes | Yes | Yes |
| Card Priority/Randomizer Test | `test_randomized_play_yields` | N/A | Yes | Yes | Yes |
| Adding/Removing Card Test | `test_add_and_remove_card` | N/A | Yes | Yes | Yes |
| Program Flow Test | `test_actions_main_runs` | N/A | Yes | Yes | Yes |
| End Tally Test | `test_session_count` | N/A | N/A | Yes | Yes |
| Empty CSV Test | `test_main_empty_csv` | N/A | N/A | N/A | Yes |
| File Selection Test | `test_choose_existing_file` | N/A | N/A | N/A | Yes |
| New File Creation Test | `test_create_new_file` | N/A | N/A | N/A | Yes |
| File Empty Folder Test | `test_empty_folder` | N/A | N/A | N/A | Yes |