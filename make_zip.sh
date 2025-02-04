#!/bin/bash

# Define the name of the zip file
ZIP_FILE="lambda_function.zip"

# Remove the existing zip file if it exists
if [ -f "$ZIP_FILE" ]; then
  rm "$ZIP_FILE"
fi

# Create a new zip file with the contents of the current directory
mkdir -p build

cp -r venv/lib/python3.13/site-packages/* build/
cp *.py build/
cp requirements.txt build/

cd build || exit
zip -r "../$ZIP_FILE" .
cd ..

echo "Created $ZIP_FILE for AWS Lambda function."
