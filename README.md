📁 SortMyFiles

**SortMyFiles** is a Python script designed to declutter and organize your folders by automatically sorting files into categorized subfolders based on their file extensions.

✨ Features

* **Automatic Categorization**: Sorts files into predefined categories such as Documents, Images, Videos, Music, Archives, Code files, and more.
* **Duplicate Handling**: Detects duplicate filenames and appends a counter to prevent overwriting.
* **Empty Folder Cleanup**: Removes empty directories post-organization to maintain a tidy structure.
* **GUI Integration**: Utilizes Tkinter for a user-friendly folder selection dialog.
* **Extensive File Type Support**: Recognizes a wide range of file extensions across various categories.

## 📂 Supported Categories

* **Documents**: `.doc`, `.docx`, `.txt`, `.pdf`, `.rtf`, `.odt`, `.tex`, `.md`, `.log`, `.wps`, `.wpd`, `.asc`, `.ans`, `.json`, `.yaml`, `.yml`, `.ini`, `.cfg`, `.conf`, `.nfo`
* **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
* **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`
* **Music**: `.mp3`, `.wav`, `.ogg`
* **Archives**: `.zip`, `.rar`, `.gz`, `.bz2`
* **Code Files**:

  * **C**: `.c`, `.h`
  * **Python**: `.py`, `.pyc`
  * **Java**: `.java`, `.class`
  * **JavaScript**: `.js`
  * **HTML**: `.html`, `.htm`
  * **CSS**: `.css`
* **Molecular Formats**:

  * **Avogadro**: `.cjson`, `.xyz`, `.pdb`, `.mol`
  * **Chimera**: `.mae`, `.mol2`, `.sdf`
  * **AutoDockTools**: `.dlg`, `.pdbqt`
  * **Discovery Studio**: `.cif`, `.sdf`
* **Executables**: `.exe`, `.bin`
* **Excel and Data Files**: `.xls`, `.xlsx`, `.xlsm`, `.xlsb`, `.xlt`, `.xltx`, `.xltm`, `.ods`, `.csv`, `.tsv`
* **Other**: Files that don't match any predefined category

## 🛠️ How to Use

### Prerequisites

* Python 3.x installed on your system.

### Running the Script

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Sag12datasci/SortMyFiles.git
   cd SortMyFiles
   ```

2. **Execute the Script**:

   ```bash
   python folder_organizer.py
   ```

3. **Select Folder**:

   * A GUI dialog will appear prompting you to select the folder you wish to organize.

4. **Organization Process**:

   * The script will sort files into their respective category folders within the selected directory.

5. **Completion**:

   * Upon completion, a message will indicate that the organization is complete.

## 🖼️ Example

**Before**:

```
Downloads/
├── report.docx
├── photo.jpg
├── song.mp3
├── script.py
```

**After**:

```
Downloads/
├── Documents/
│   └── report.docx
├── Images/
│   └── photo.jpg
├── Music/
│   └── song.mp3
├── Python/
    └── script.py
```

## ⚠️ Notes

* **File Movement**: Files are moved to their respective folders; ensure you have backups if necessary.
* **Hidden Files**: Files starting with a dot (`.`) are ignored to prevent unintended moves.
* **System Folders**: Avoid running the script on system-critical directories.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
