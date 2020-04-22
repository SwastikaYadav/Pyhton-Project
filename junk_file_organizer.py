import os
from pathlib import Path #pip

DIRECTORIES = {"HTML/CSS"  :   [".html", ".HTML", ".xhtlm", ".html5", ".xml", "CSS", ".shtml"],
               "IMAGES": [".jpeg", "jpg", ".tiff", "heif", ".psd", "bpg", ".mpeg",".png"],
               "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", "3gp", "mpeg"],
               "DOCUMENTS": [".oxps", "epub", ".pages", ".docx", ".doc", ".doc", "fdf", "ods", "odt",
                             "pwi", ".xps", "dotx", "docm", ".dox", ".rvg", ".rtf", ".wpd", ".xls" , ".xlsx", ".ppt", "pptx"],
               "ARCHIEVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", "7z", ".exe", ".dmg", ".rar", ".xar", ".zip"],
               "AUDIOS" : [".aac", ".aa", ".aac", ".dvf", ".mp3", ".m4a", ".m4b", ".m4p"],
               "TEXT-FILES" : [".txt", ".in",".out"],
               "PDFS" : [".pdf"],
               "PYTHON": [".py"],
               "C-CPP": [".c", ".cpp"],
               "JAVA": [".jsp", ".jspx", ".was", ".do", ".action"],
               "JAVASCRIPT": [".js"],
               "XML": [".xml", ".rss", ".svg"],
               "PHP": [".php", ".php4", ".php3", ".phtml"],
               "SHELL":[".shell"],
               "APPICATIONS" : [".apk"]
}

FILE_FORMATS = { file_format : directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats }

def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
    try:
        os.mkdir("OTHER-FILES")
    except:
        pass

    for dir in os.scandir() :
        try:
            if dir.is_dir() :
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER-FILES/' + str(Pth(dir)))
        except:
            pass

if __name__ == "__main__":
    organize_junk()
