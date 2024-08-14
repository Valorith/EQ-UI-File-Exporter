import os
import re
import shutil
import configparser


# Define default settings
default_settings = {
    'Settings': {
        'export_dir': 'ExportedUIFiles',
        'target_server_short_name': 'CWTest',
        'source_server_short_name': 'CWR'
    }
}

# Check if exporter.ini exists
ini_file = 'exporter.ini'
if not os.path.exists(ini_file):
    # Create exporter.ini with default settings
    config = configparser.ConfigParser()
    config.read_dict(default_settings)
    with open(ini_file, 'w') as configfile:
        config.write(configfile)
    print(f"{ini_file} created with default settings.")


# Load settings from exporter.ini
config = configparser.ConfigParser()
config.read('exporter.ini')

# Example of accessing settings
# Assuming exporter.ini has a section [Settings] with a key 'export_dir'
print(f"Loading app settings from {ini_file}.")
export_dir = config.get('Settings', 'export_dir', fallback='ExportedUIFiles')
print(f"Export directory loaded: {export_dir}")
target_server_short_name = config.get('Settings', 'target_server_short_name', fallback='CWTest')
print(f"Target server short name loaded: {target_server_short_name}")
source_server_short_name = config.get('Settings', 'source_server_short_name', fallback='CWR')
print(f"Source server short name loaded: {source_server_short_name}")

# Define the patterns to search for
pattern1 = re.compile(r'UI_(\w+)_CWR\.ini')
pattern2 = re.compile(r'(\w+)_CWR\.ini')

# Get the current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Find all files matching the patterns
files = [f for f in os.listdir(current_dir) if pattern1.match(f) or pattern2.match(f)]
print(f"Found {len(files)} files matching the patterns.")

# Extract character names from the filenames
char_names = set()
for file in files:
    match1 = pattern1.match(file)
    match2 = pattern2.match(file)
    if match1:
        char_names.add(match1.group(1))
    elif match2:
        char_names.add(match2.group(1))
print(f"Extracted character names: {char_names}")

# Create the required sub-directory structure
export_dir = os.path.join(current_dir, export_dir)
os.makedirs(export_dir, exist_ok=True)
print(f"Created export directory: {export_dir}")

all_dir = os.path.join(export_dir, 'ALL')
os.makedirs(all_dir, exist_ok=True)
print(f"Created ALL export directory: {all_dir}")

for char_name in char_names:
    char_dir = os.path.join(export_dir, char_name)
    os.makedirs(char_dir, exist_ok=True)
    print(f"Created export directory for character {char_name}: {char_dir}")

# Copy and rename the files to the appropriate sub-directories
for char_name in char_names:
    ui_file = f'UI_{char_name}_{target_server_short_name}.ini'
    char_file = f'{char_name}_{target_server_short_name}.ini'
    print(f"Checking files for character {char_name}: {ui_file}, {char_file}")
    
    if ui_file in files:
        new_ui_file_name = ui_file.replace('_CWR', f"_{target_server_short_name}")
        
        # Copy to ALL directory
        shutil.copyfile(os.path.join(current_dir, ui_file), os.path.join(all_dir, new_ui_file_name))
        print(f"Copied {ui_file}...")
        
        # Copy to character-specific directory
        char_dir = os.path.join(export_dir, char_name)
        shutil.copyfile(os.path.join(current_dir, ui_file), os.path.join(char_dir, new_ui_file_name))
        print(f"Copied {ui_file}...")
    else:
        print(f"File not found: {ui_file}")
    
    if char_file in files:
        new_char_file_name = char_file.replace('_CWR', f"_{target_server_short_name}")
        
        # Copy to ALL directory
        shutil.copyfile(os.path.join(current_dir, char_file), os.path.join(all_dir, new_char_file_name))
        print(f"Copied {char_file}...")
        
        # Copy to character-specific directory
        char_dir = os.path.join(export_dir, char_name)
        shutil.copyfile(os.path.join(current_dir, char_file), os.path.join(char_dir, new_char_file_name))
        print(f"Copied {char_file}...")
    else:
        print(f"File not found: {char_file}")

print("Files have been successfully copied and renamed.")
input("Press any key to exit...")