#Talk is a python script to transcribe audio and video in .txt file, its use Whisper from Open AI.
import subprocess

# Installer le package whisper
subprocess.call(['pip', 'install', 'git+https://github.com/openai/whisper.git'])

# Mettre à jour la liste des paquets disponibles et installer ffmpeg
subprocess.call(['sudo', 'apt', 'update'])
subprocess.call(['sudo', 'apt', 'install', 'ffmpeg'])

subprocess.call(['whisper', 'Nom_fichier.extension', '--model', 'large'])
