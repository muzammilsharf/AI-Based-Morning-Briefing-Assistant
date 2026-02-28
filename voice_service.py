import edge_tts
import asyncio
import pygame
import os

VOICE = "ur-PK-AsadNeural" 

async def text_to_speech(text, output_file="greeting.mp3"):
    """Converts Urdu text to an MP3 file using Edge-TTS."""
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

def play_audio(file_path):
    """Plays the generated MP3 file."""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

def speak(text):
    """The main function called by your AI Agent."""
    if not text:
        return
    
    # Run the async TTS conversion
    asyncio.run(text_to_speech(text))
    
    # Play the file
    play_audio("greeting.mp3")
    
    # Clean up the file to keep your folder tidy
    if os.path.exists("greeting.mp3"):
        os.remove("greeting.mp3")
