import random
feet_in_mile = 5280
meters_in_kilometer = 1000
YouTuber = ["Michael Steven", "Jimmy Donaldson", "SrPel"]

def get_file_extension(file_name):
    return file_name[file_name.index(".")+1:]

def roll_dice(num):
    return random.randint(1, num)

