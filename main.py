from pathlib import Path
import shutil

Downloads = Path.home() / 'Downloads'
print(Downloads/'filename')
lst = []

# disk image (.dmg)
# .html, .pkg, .tex, .zip?

# Moves file from the downloads folder to the correct destination folder
def move_file(file, dest):
    shutil.move(Downloads/file, Downloads/dest/file)

for entry in Downloads.iterdir():
    if entry.is_file():
        # print(Path.home() / 'Downloads' / entry.name)
        # if len(entry.name) >= 35:
        #     pass
        if Path(entry).suffix.lower() in ['.png','.heic','.jpg','.jpeg','.webp']:
            if 'screenshot' in entry.name.lower():
                # Move to screenshots folder within photos folder
                pass
            else:
                # Move to photos folder
                # print(entry.name)
                pass
        elif Path(entry).suffix in ['.mov', '.MOV']:
            # Move to videos/movies folder
            pass
        elif Path(entry).suffix in ['.m4a', '.mp4', '.mp3']:
            # Move to music folder
            pass
        elif Path(entry).suffix in ['.rkt','.rkt~']:
            # Move to racket folder
            pass
        elif Path(entry).suffix == '.c':
            # Move to C folder
            pass
        elif Path(entry).suffix in ['.m4a', '.mp4', '.mp3']:
            # Move to music folder
            pass
        elif Path(entry).suffix == '.pkg':
            # Move to packages folder
            pass
        elif Path(entry).suffix in ['.doc','docx','.pages','.pdf']:
            if 'resume' in entry.name.lower():
                # Move to resume folder in personal folder in documents folder
                pass
            if 'cover letter' in entry.name.lower():
                # Move to cover letter folder in personal folder in documents folder
                pass
            elif 'grade report' in entry.name.lower():
                # Move to grade report folder in personal folder in documents folder
                pass
            elif 'work term record' in entry.name.lower():
                # Move to personal files folder in personal folder in documents folder
                pass
            elif 'T4A' in entry.name:
                # Move to personal files folder in personal folder in documents folder
                print(entry.name)
                pass
            elif 'T2202' in entry.name:
                # Move to personal files folder in personal folder in documents folder
                print(entry.name)
                pass
            elif 'PD' in entry.name:
                # Move to PD folder in school folder in documents folder
                pass
            elif 'comms' in entry.name.lower():
                # Move to comms223 folder in school folder in documents folder
                pass
            elif 'Econ' in entry.name:
                # Move to econ folder in school in documents folder
                pass
            elif 'written assignment' in entry.name.lower():
                # Move to written assignments folder in math folder in school folder in documents folder
                pass
            elif 'möbius' in entry.name.lower():
                # Move to mobius folder in math folder in school folder in documents folder
                pass
            elif 'mobius' in entry.name.lower():
                # Move to mobius folder in math folder in school folder in documents folder
                pass
            else:
                # Move to documents folder
                pass
        else:
            # Move to random/unknown folder
            pass