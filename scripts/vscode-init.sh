#!/usr/bin/env bash

# Initialise a .vscode directory within the working directory, and create the
# usual files if they don't exist.

make_file_with_content() {
    if [ ! -f "$1" ]; then
        echo "$2" > "$1"
    fi
}

LAUNCH_TEMPLATE='{
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": []
}'
TASKS_TEMPLATE='{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": []
}'

mkdir -p ".vscode"
make_file_with_content ".vscode/settings.json" '{}'
make_file_with_content ".vscode/.gitignore" '*'
make_file_with_content ".vscode/launch.json" "${LAUNCH_TEMPLATE}"
make_file_with_content ".vscode/tasks.json" "${TASKS_TEMPLATE}"
