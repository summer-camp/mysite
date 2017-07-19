import game


def test_win():
    word = "abcdef"
    state = game.reset_state(word)
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        state = game.turn(state, letter)

    assert state['errors'] == 0
    expected_turns = game.MAX_ERRORS
    expected_message = "You win, word was '%s'. You had %s turns left" % (
        word, expected_turns)

    assert state['message'] == expected_message

def _print_state(state):
    for k, v in state.items():
        print "%20s %s" % (k, v)

def test_loose():
    word = "wxyz"
    state = game.reset_state(word)
    _print_state(state)
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        state = game.turn(state, letter)

    assert state['errors'] == game.MAX_ERRORS
    expected_message = "You LOOSE, word was '%s'" % word
    assert state['message'] == expected_message

def test_2_errors():
    word = "abcdef"
    state = game.reset_state(word)
    for letter in ['a', 'b', 'c', 'w', 'p', 'd', 'e', 'f']:
        state = game.turn(state, letter)

    assert state['errors'] == 2

    expected_turns = game.MAX_ERRORS - 2
    expected_message = "You win, word was '%s'. You had %s turns left" % (
        word, expected_turns)
    assert state['message'] == expected_message
