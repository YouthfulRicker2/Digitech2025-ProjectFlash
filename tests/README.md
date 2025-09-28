# Testing the Program 

## With pytest:

To run test programs run `pytest -v` in your shell while the base directory is your working directory.

### [test_data.py](test_data.py)

This program first imports the data functions, then it utilizes `fileManagement.create_csv()` to first create a temp csv, then it uses `fileManagement.add_card()` to add a card to the csv. The test then verifies that the csv contains the added example card. It then removes the card using `fileManagement.remove_card()` and verifies that there is no card. Afterward it removes the temp csv to complete the process.

### [test_actions.py](test_actions.py)

This test module imports the `studyTime` class of [actions.py](actions.py) and then defines two dummy helpers (`dummyInput` & `dummyTime`) to spoof user input and user time taken respectively.\
The first test (`test_ask_card_leitner_timing`) first uses `monkeypatch` to spoof the existence of a csv using a test-defined dictionary, and creates a tuple to log expected end leitner value and required input. It asserts that the end leitner result for the card is as expected.\
The second test (`test_randomized_play_yields`) builds a spoof dictionary deck with expected states for primary (`1`-`3`) and secondary (`4`-`5`) leitner values. It simulates every card getting a quick answer and thus makes sure that each card was yielded only once.

#### Additions

- [ ] Test `cardParse` class.

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


## Testing
Tests can be simply run by installing and running `pytest` in Kādo program's root folder.\

iteration1 = Commit ID: [b19f1f1296ebb3e34016be64353b91a19a4026a2](https://github.com/YouthfulRicker2/Digitech2025-ProjectFlash/commit/b19f1f1296ebb3e34016be64353b91a19a4026a2)\
iteration2 = Commit ID: [98c131eae39c3d1e32b5677422061607361fd6e7](https://github.com/YouthfulRicker2/Digitech2025-ProjectFlash/commit/98c131eae39c3d1e32b5677422061607361fd6e7)\

N/A indicates that the feature wasn't implemented or tested in that iteration.

iteration1 was not tested due to the tests not being fully developed at that stage. They were developed alongside and completed slightly after iteration2.

| Test Friendly Name | Test ID | iteration1 | iteration2 |
|-------------------------------|-------------------------------|-------------|-------------|
| Leitner System Timing Test | `test_ask_card_leitner_timing` | N/A | Yes |
| Card Priority/Randomizer Test | `test_randomized_play_yields` | N/A | Yes |
| Adding/Removing Card Test | `test_add_and_remove_card` | N/A | Yes |
| Program Flow Test | `test_actions_main_runs` | N/A | Yes |