# Documentation

FlashQuiz is a study tool Python package for practicing flashcards

Quizzing yourself on flashcards is not supported yet as of v0.01, but it is planned to be added in the future.

## Installation

> pip install flashquiz


## Running

Open the terminal and run

> flashquiz [args]


## Args

| Argument        | Behavior                                                      | Default                         |
|-----------------|---------------------------------------------------------------|---------------------------------|
| `--file`        | .csv file containing questions and answers for the flashcards | flashquiz/default.csv           |
| `--font`        | Sets the font for all text (must be pygame-supported)         | inkfree                         |
| `--cards_front` | .jpg file to use as the background for cards' front           | flashquiz/assets/card_front.jpg |
| `--cards_back`  | .jpg file to use as the background for cards' back            | flashquiz/assets/card_back.jpg  |
| `--h`           | Sets the window height                                        | 500                             |
| `--w`           | Sets the window width                                         | 700                             |
| `--title`       | Changes the window title                                      | FlashQuiz                       |
| `--fps`         | Set the fps for the window to run at                          | 30                              |
