#!/bin/bash

# Check if the script is provided with a URL argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL to download
URL="$1"

# Log file
LOG_FILE="log.txt"

# Date and time for the log entry
LOG_ENTRY_DATE=$(date "+%Y-%m-%d %H:%M:%S")

# Download the URL using wget
wget "$URL" -O "downloaded_file"

# Check the exit status of wget
if [ $? -eq 0 ]; then
    # If successful, append a log entry to the log file
    echo "[$LOG_ENTRY_DATE] Downloaded: $URL" >> "$LOG_FILE"
    echo "Download complete"
else
    # If unsuccessful, append an error log entry to the log file
    echo "[$LOG_ENTRY_DATE] Error downloading: $URL" >> "$LOG_FILE"
    echo "Download filed"
fi


