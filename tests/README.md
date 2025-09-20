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