from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and tell the player to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and tell the player to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_numeric_comparison_not_lexicographic():
    # As strings "9" > "10", but numerically 9 < 10
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"

def test_parse_valid_guess_in_range():
    assert parse_guess("15", 1, 20) == (True, 15, None)

def test_parse_range_boundaries_are_inclusive():
    assert parse_guess("1", 1, 20) == (True, 1, None)
    assert parse_guess("20", 1, 20) == (True, 20, None)

def test_parse_guess_above_range():
    ok, value, err = parse_guess("21", 1, 20)
    assert not ok
    assert value is None
    assert "between 1 and 20" in err

def test_parse_guess_below_range():
    ok, value, err = parse_guess("0", 1, 20)
    assert not ok
    assert value is None
    assert "between 1 and 20" in err

def test_parse_negative_guess_out_of_range():
    ok, _, _ = parse_guess("-5", 1, 100)
    assert not ok

def test_parse_non_number():
    assert parse_guess("abc", 1, 20) == (False, None, "That is not a number.")

def test_parse_empty():
    assert parse_guess("", 1, 20) == (False, None, "Enter a guess.")

def test_regression_guess_50_secret_40_says_go_lower():
    # Bug: guessing 50 when the secret was 40 said "Go HIGHER" instead of "Go LOWER".
    # The hint messages were swapped, and on even attempts the secret was turned into a
    # string, so the comparison was done on text instead of numbers.
    outcome, message = check_guess(50, 40)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_regression_guess_110_rejected_on_normal_range():
    # Bug: entering 110 on Normal difficulty (range 1-100) was accepted as a valid guess.
    ok, value, err = parse_guess("110", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."
