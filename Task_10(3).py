+----------------+
|  MusicPlayer   |
+----------------+
| - playlist: Playlist      |
| - volume: float           |
| - current_track: Track    |
+----------------+
| + play()                  |
| + pause()                 |
| + stop()                  |
| + next_track()            |
| + previous_track()        |
| + set_volume(volume: float)|
| + get_volume() -> float   |
| + get_current_track() -> Track |
+----------------+

+----------------+
|     Track      |
+----------------+
| - title: str   |
| - artist: str  |
| - duration: int|
+----------------+
| + get_info() -> str|
+----------------+

+----------------+
|    Playlist    |
+----------------+
| - tracks: List[Track]  |
| - repeat_mode: bool    |
+----------------+
| + add_track(track: Track) |
| + remove_track(track: Track)|
| + get_tracks() -> List[Track] |
| + shuffle()          |
+----------------+



from typing import List

class Track:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_info(self) -> str:
        return f"{self.title} by {self.artist}, Duration: {self.duration}s"

class Playlist:
    def __init__(self):
        self.tracks = []
        self.repeat_mode = False

    def add_track(self, track: Track):
        self.tracks.append(track)

    def remove_track(self, track: Track):
        self.tracks.remove(track)

    def get_tracks(self) -> List[Track]:
        return self.tracks

    def shuffle(self):
        import random
        random.shuffle(self.tracks)

class MusicPlayer:
    def __init__(self):
        self.playlist = Playlist()
        self.volume = 0.5
        self.current_track = None

    def play(self):
        if self.current_track:
            print(f"Playing: {self.current_track.get_info()}")
        else:
            print("No track selected to play.")

    def pause(self):
        if self.current_track:
            print(f"Paused: {self.current_track.get_info()}")
        else:
            print("No track selected to pause.")

    def stop(self):
        if self.current_track:
            print(f"Stopped: {self.current_track.get_info()}")
            self.current_track = None
        else:
            print("No track selected to stop.")

    def next_track(self):
        if self.playlist.tracks:
            self.current_track = self.playlist.tracks[0]
            print(f"Next track: {self.current_track.get_info()}")
        else:
            print("No tracks in playlist.")

    def previous_track(self):
        if self.playlist.tracks:
            self.current_track = self.playlist.tracks[-1]
            print(f"Previous track: {self.current_track.get_info()}")
        else:
            print("No tracks in playlist.")

    def set_volume(self, volume: float):
        if 0 <= volume <= 1:
            self.volume = volume
            print(f"Volume set to: {self.volume * 100}%")
        else:
            print("Volume must be between 0 and 1.")

    def get_volume(self) -> float:
        return self.volume

    def get_current_track(self) -> Track:
        return self.current_track

