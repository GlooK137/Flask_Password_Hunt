# Base image
FROM python:3.7.16-bullseye
# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN apt update && apt install iputils-ping netcat -y
RUN pip install cx_Freeze
RUN pip install -r requirements.txt
# Copy the Flask app code to the working directory
COPY src/. .

RUN python -m cx_Freeze app.py
RUN mv build/exe.linux-x86_64-3.7/app build/exe.linux-x86_64-3.7/lib .
RUN rm -rf build app.py

# Expose the default Flask port
EXPOSE 80

# Run the Flask app on port 80
CMD ["./app"]
