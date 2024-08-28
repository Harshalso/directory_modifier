import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    try:
      
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

       
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            
          
            if os.path.isfile(source_file):
                destination_file = os.path.join(destination_dir, filename)

               
                if os.path.exists(destination_file):
                    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    name, ext = os.path.splitext(filename)
                    destination_file = os.path.join(destination_dir, f"{name}_{timestamp}{ext}")

              
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {filename} to {destination_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_dir = sys.argv[1]
        destination_dir = sys.argv[2]
        backup_files(source_dir, destination_dir)
