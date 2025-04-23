from pygame import mixer

# Initialize pygame sound system
mixer.init()

# Load and play each sound
print("Playing win.wav...")
mixer.Sound("game/assets/win.wav").play()
input("Press Enter to continue...")

print("Playing lose.wav...")
mixer.Sound("game/assets/lose.wav").play()
input("Press Enter to continue...")

print("Playing tie.wav...")
mixer.Sound("game/assets/tie.wav").play()
input("Done. Press Enter to exit.")
