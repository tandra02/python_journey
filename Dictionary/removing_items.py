'''You're given a dictionary representing a playlist of songs and their durations. Your task is to modify the playlist by updating the durations of existing songs, adding new songs, and removing specific songs. Perform the following updates:

Update the duration of "Song1" to 200 seconds.
Add a new song, "Song5," with a duration of 220 seconds.
Update the duration of "Song2" to 195 seconds.
Remove "Song3" from the playlist.'''

# The playlist dictionary
playlist = {
    "Song1": 180,  # Duration in seconds
    "Song2": 210,
    "Song3": 160,
    "Song4": 190
}

# Your code here
playlist.update({"Song1": 200})
playlist["Song5"] = 220
playlist.update({"Song2": 195})
playlist.pop("Song3")
# Don't change below this line
print("Updated Playlist:", playlist)
