# Assignment Template creater

This is a Command Line Interface (CLI) created using python. Using this you can create all necessary files for writing your assignment report.

I created this because, i am not getting ready with latex to create PDF, so i think of an alternative. What about creating PDF from our favourite markdown language!!

## Pre-requisites
1. VScode should be installed
2. You have to install an extension in VScode -> **Markdown PDF**
3. install **Markdown All in One** extension also. 

## Installation
    pip install fire
    git clone https://github.com/rawho/assBOT.git
    cd assBOT
    

## Usage
    python assbot.py create hello

This Will create a folder hello for you, Lets take a look at the folder

    hello
    |--cet-logo.jpeg
    |--demo.png
    |--hello.md

In the `hello.md` file you can see  a template will be created, There you can change the name, heading, etc..

`demo.png` and `cet-logo.jpeg` are the images used, you can add new images to this folder and add it in the markdown file

## Convert to PDF
- Open the `hello.md` file in VScode
- `ctl + shift + p` and search **export**, then select **Markdown PDF: Export (pdf)** 

Then Wait for few seconds and you can see a new pdf file is created in the same folder.


## Few Tips
- Probably if you follow above steps, You will get a pdf file, Inside it you can see that the code snippets is not highlighted, inorder to enable it, you can change the settings of the extension **Markdown PDF**
 
    for that press `ctl + ,` it will open the settings.

    from there go to **extensions** and **markdown pdf**, scroll down and  change the highlight style. There is a dropdown. You can select any one from it. My suggestion is *a11y-dark.css*
- for converting to pdf instead of searching, you can just right-click, there you can see the option to export
