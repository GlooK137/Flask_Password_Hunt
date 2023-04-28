# Flask_Password_Hunt

## Description

- I was motivated to create this ctf job by the lack of good code security in python 3.8 and the misconception of developers about code security, especially those who write important information directly in the code.
- With this project, I would like to show that for security of any system or product, it is necessary to use services and programs of the latest versions, and not to use vital (access tokens, passwords) in the code.
- By studying cx_Freeze (a free package for creating self-sufficient Python binaries on different platforms) I learned how to get the source code of an application.
- Now on to how to get it all up and running and trying it out.

## Installation
1. Clone this repository to your local machine:
`git clone https://github.com/GlooK137/Flask_Password_Hunt`
2. Change into the project directory:
`cd Flask_Password_Hunt`
## Running
1. Build the Docker image:
`docker build -t flask_password_hunt .`
2. Run the Docker container:
`docker run -d -p 80:80 --name fph flask_password_hunt`
3. Access the application through your web browser at `http://localhost:80`
4. Start solving the CTF challenge and find the hidden flag!

