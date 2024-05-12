import obspython as obs
from datetime import datetime
shot_number = 1

def set_shot_number(props, prop):
    global shot_number
    shot_number = obs.obs_properties_get(props, "shot_number")
    update_filename_format()

def update_filename_format():
    global shot_number
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    shot_number = int(shot_number)
    # Format the string with shot number and current date and time
    if shot_number < 10:
        shot_number_str = "Shot0{} ".format(shot_number)
    else:
        shot_number_str = "Shot{} ".format(shot_number)
    
    # Construct the format string by concatenating the components
    format_string = shot_number_str + current_time
    
    settings = config = obs.obs_frontend_get_profile_config()
    
    # Assuming 'Advanced' is a group in the settings
    advanced_settings = obs.config_get_string(config, "Output",
                                                         "FilenameFormatting")
        
    obs.config_set_string(config, "Output",
                                  "FilenameFormatting", format_string)
    
    # Set the Filename Formatting value in the recording settings
        
        

    
    

def script_description():
    return "Sets the filename formatting based on the current scene's shot number"

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_int(props, "shot_number", "Shot Number", 1, 999, 1)
    obs.obs_properties_add_button(props, "button", "Set Shot Number", set_shot_number)
    return props

def script_update(settings):
    update_filename_format()
