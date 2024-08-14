[How to Run]

- Place the exe in the same directory as your eq client.
- Run the exe
- Thats it!

[Access exported files]

- After you have run the script, you should see a newly created sub-directory called `ExportedUIFiles` (default value, can be changed in `exporter.ini`)
  - This directory will have some organized sub-directories (All, CharName1, CharName2, etc).
  - The `All` directory will show all exported UI files for every character found.
  - The named folders will be specific to each character that had UI files in your EQ directory.
  - All of the server short name suffixes will be changed, consistant with your settings (`exporter.ini`).
    - For example: `SilverFox_CWR.ini` => `SilverFox_CWTest.ini`
    - These suffix names can be set in `exporter.ini`: `source_server_short_name` and `target_server_short_name`
    - Default values are: `source_server_short_name` = "CWR" and `target_server_short_name` = "CWTest"

[Compile]

- You only need to compile your own binaries if you want to modify the application. If you just want to use the app, you can simply use the Release binaries.
- I use a package called pyinstaller to compile this python script into a binary file. You can alternatively just run the script in place (will need Python installed).
- Once you have installed `pyinstaller` (https://pyinstaller.org), you can run the following command to compile binaries: `pyinstaller main.py -F --uac-admin -i Old_eq_icon.ico`
