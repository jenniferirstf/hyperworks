import subprocess
import os

def list_power_plans():
    """List all available power plans"""
    command = 'powercfg /list'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print("Available Power Plans:\n", result.stdout)

def set_power_plan(plan_guid):
    """Set the active power plan by its GUID"""
    command = f'powercfg /setactive {plan_guid}'
    subprocess.run(command, shell=True)
    print(f"Power plan set to {plan_guid}")

def create_power_plan(name, description, base_plan_guid):
    """Create a new custom power plan"""
    command = f'powercfg /duplicatescheme {base_plan_guid}'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    new_plan_guid = result.stdout.strip()
    
    command = f'powercfg /changename {new_plan_guid} "{name}" "{description}"'
    subprocess.run(command, shell=True)
    print(f"Created new power plan: {name} with GUID: {new_plan_guid}")

def delete_power_plan(plan_guid):
    """Delete an existing power plan by its GUID"""
    command = f'powercfg /delete {plan_guid}'
    subprocess.run(command, shell=True)
    print(f"Deleted power plan: {plan_guid}")

def get_current_settings():
    """Get current power settings"""
    command = 'powercfg /q'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print("Current Power Settings:\n", result.stdout)

def main():
    print("HyperWorks Power Management")
    list_power_plans()
    
    # Example usage:
    # set_power_plan('GUID')
    # create_power_plan('New Plan', 'Description', 'Base GUID')
    # delete_power_plan('GUID')
    # get_current_settings()

if __name__ == "__main__":
    main()