# Base Image
FROM python:latest

# Upgrade pip
RUN pip install --upgrade pip

# Install Path
ENV APP_PATH /WAS

# Install Python modules needed by the Python app
COPY requirements.txt $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt

# Copy files required for the app to run
COPY app.py $APP_PATH/
COPY templates/ $APP_PATH/templates/
COPY static/ $APP_PATH/static/

# Port number the container should expose
EXPOSE 8080

# Run the application
CMD ["python", "/WAS/app.py"]
