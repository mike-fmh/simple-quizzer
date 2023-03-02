# Documentation

## Installation

> pip install flashquiz


## Running

> cd /path-to-python/site-packages/flashquiz
> python quizzer.py [args]


## Args

| Argument        | Behavior                                                      | Default                           |
|-----------------|---------------------------------------------------------------|-----------------------------------|
| `--file`        | .csv file containing questions and answers for the flashcards | default.csv (included in package) |
| `--font`        | Sets the font for all text (must be pygame-supported)         | inkfree                           |
| `--cards_front` | .jpg file to use as the background for cards' front           | assets/card_front.jpg             |
| `--cards_back`  | .jpg file to use as the background for cards' back            | assets/card_back.jpg              |
| `--h`           | Sets the window height                                        | 500                               |
| `--w`           | Sets the window width                                         | 700                               |
| `--title`       | Changes the window title                                      | FlashQuiz                         |
| `--fps`         | Set the fps for the window to run at                          | 30                                |
