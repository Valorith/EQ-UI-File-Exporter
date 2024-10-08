# [How to Run]

- Download the release binaries from the Release section on the right side of the repository page.
- ![image](https://github.com/user-attachments/assets/fffa6c87-83b9-4f7f-8e40-5710d9908b77)
- Place the exe in the same directory as your eq client.
- Run the exe
- Thats it!

# [Access exported files]

- After you have run the script, you should see a newly created sub-directory called `<EQDirectory>/ExportedUIFiles` (default value, can be changed in `exporter.ini`)
  - This directory will have some organized sub-directories (All, CharName1, CharName2, etc).
  - ![image](https://github.com/user-attachments/assets/2fb2b251-5de8-4e07-b38a-c614cfb08687)
  - The `All` directory `<EQDirectory>/ExportedUIFiles/ALL` will show all exported UI files for every character found.
  - ![image](https://github.com/user-attachments/assets/931508db-3268-4055-b7df-83180d25c025)
  - The named folders, example: `<EQDirectory>/ExportedUIFiles/Valdor`, will be specific to each character that had UI files in your EQ directory.
  - ![image](https://github.com/user-attachments/assets/075fb338-dbce-4439-8cd4-ebbdc6aa44d8)
  - All of the server short name suffixes will be changed, consistant with your settings (`exporter.ini`).
    - For example: `SilverFox_CWR.ini` => `SilverFox_CWTest.ini`
    - These suffix names can be set in `exporter.ini`: `source_server_short_name` and `target_server_short_name`
    - Default values are: `source_server_short_name` = "CWR" and `target_server_short_name` = "CWTest"

# [Compile]

- THIS IS NOT REQUIRED! You only need to compile your own binaries if you want to change the application.
- If you just want to USE the default app, you can simply use the Release binaries.
- I use a package called `pyinstaller` to compile this python script into a binary file. You can alternatively just run the script in place (will need Python installed: https://www.python.org/downloads/).
- Once you have installed `pyinstaller` (https://pyinstaller.org), you can run the following command to compile binaries: `pyinstaller main.py -F --uac-admin -i Old_eq_icon.ico`
 - Your exe will be saved in `<project_folder/dist/main.exe`
