from app import process_query

def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == ("Dinosaurs rulled the Earth 200 million years ago")

def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"

