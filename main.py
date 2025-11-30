import yt_dlp
tmpDownloadFileLocation = "C:/Users/Aaron-Desktop/Downloads/tmpytdlpDownloads/"
downloadFileLocation = "C:/Users/Aaron-Desktop/Downloads/ytdlpDownloads/"
convertedFileLocation = "C:/Users/Aaron-Desktop/Downloads/ytdlpDownloads/convertedFiles"
outputFileLocation = "*/path/to/output/folder"


# Get List of YTIDs for batch download
cookiesFileLocation = "C:/Users/Aaron-Desktop/Documents/cookies.Work.txt"
watchLater = "https://www.youtube.com/playlist?list=WL"
testYTID = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"] # Test YT ID


# Set YTDL Options for download
ytdlOptions = {
    'cookiefile': cookiesFileLocation,
    'js_runtimes' : {'node': {'path': 'C:/Program Files/nodejs'}},
    'paths': {"temp" : tmpDownloadFileLocation, "home": downloadFileLocation},
    'download_archive': 'archivetest.txt'
}

# Download YTIDs in batch
with yt_dlp.YoutubeDL(ytdlOptions) as ytdl:
    error_code = ytdl.download(watchLater)

# Output error code if any 
if error_code:
    print(f"Download encountered an error. Error code: {error_code}")
    exit(error_code)

# Convert downloaded files to iPod format


# Move converted files to output folder

# Clean up temporary files

# Notify user of completion
print("Test download finished")
