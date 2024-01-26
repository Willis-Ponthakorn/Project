import subprocess
import os

# Input video file path
input_file = 'DJI_0302.mp4'

# Output directory to save frames
output_directory = 'input/realroof5/'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# FFmpeg command to extract frames
ffmpeg_command = [
    'ffmpeg',
    '-i', input_file,             # Input video file
    '-vf', 'fps=1',               # Frame rate (e.g., 8 FPS)
    '-vsync', 'vfr',
    os.path.join(output_directory, '%04d.jpg')  # Output frame filename pattern
]

# Run FFmpeg to extract frames
subprocess.run(ffmpeg_command)