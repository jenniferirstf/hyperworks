# HyperWorks

## Overview

HyperWorks is a Python program designed to manage power settings and create custom power plans based on usage on Windows. It leverages the Windows `powercfg` command to list, set, create, and delete power plans. This utility can help streamline power management tasks, particularly for users who frequently switch between different power configurations.

## Features

- **List Power Plans**: Displays all available power plans on the system.
- **Set Power Plan**: Enables you to activate a specific power plan using its GUID.
- **Create Power Plan**: Allows creation of a new power plan based on an existing one.
- **Delete Power Plan**: Deletes a specified power plan by its GUID.
- **View Current Settings**: Shows detailed information about the current power settings.

## Requirements

- Windows operating system
- Python 3.x

## Usage

1. **List All Power Plans:**
   ```bash
   python hyperworks.py
   ```

2. **Set a Power Plan:**
   Uncomment the `set_power_plan` line in the `main()` function and provide the target plan's GUID.

3. **Create a Custom Power Plan:**
   Uncomment the `create_power_plan` line in the `main()` function, and provide a new plan name, description, and base plan GUID.

4. **Delete a Power Plan:**
   Uncomment the `delete_power_plan` line in the `main()` function and provide the target plan's GUID.

5. **Get Current Power Settings:**
   Uncomment the `get_current_settings` line in the `main()` function.

## Notes

- Ensure that you run the script with administrative privileges to modify power settings.
- Use the `list_power_plans()` function to fetch the GUID of the power plans you wish to manipulate.

## Disclaimer

Use this software at your own risk. The author is not responsible for any damage or data loss that may occur from using this software.