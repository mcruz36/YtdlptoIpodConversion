from subprocess import run
import yt_dlp
tmpDownloadFileLocation = "C:/Users/Aaron-Desktop/Downloads/tmpytdlpDownloads/"
downloadFileLocation = "C:/Users/Aaron-Desktop/Downloads/ytdlpDownloads/"
convertedFileLocation = "C:/Users/Aaron-Desktop/Downloads/convertedFiles/"
outputFileLocation = "*/path/to/output/folder"


# Get List of YTIDs for batch download
cookiesFileLocation = "C:/Users/Aaron-Desktop/Documents/cookies.Work.txt"
watchLater = "https://www.youtube.com/playlist?list=WL"
testYTID = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"] # Test YT ID


# Set YTDL Options for download
ytdlOptions = {
    #'cookiefile': cookiesFileLocation,
    'cookiesfrombrowser': ("firefox","tpy6neil.default-release", None),
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
# Format based on https://github.com/adhikary97/ipod-formatter
testFile = "C:/Users/Aaron-Desktop/Downloads/ytdlpDownloads/A.webm"
runString = f"C:/Users/Aaron-Desktop/Downloads/ffmpeg-8.0-essentials_build/bin/ffmpeg.exe -i {testFile} -profile:v baseline -level 3.0 -b:v 1500k -c:a aac -bufsize 3000k -b:a 128k -ar 22050 -ac 1 -vf scale=640:480 {convertedFileLocation}outputfile.mp4"
# run(["C:/ffmpeg/bin/ffmpeg.exe", "-i", f"{downloadFileLocation}inputfile.mp4", "-c:v", "libx264", "-profile:v", "baseline", "-level", "3.0", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-vf", "scale=640:480", f"{convertedFileLocation}outputfile.mp4"])
print(runString)
run(runString, shell=True)


# Move converted files to output folder

# Clean up temporary files

# Notify user of completion
print("Test download finished")
