# Recursively list files and directories under /content
!find /content -type f
# Zip the entire /content folder (or a subfolder)
!zip -r content_backup.zip /content

# Download the ZIP
from google.colab import files
files.download('content_backup.zip')