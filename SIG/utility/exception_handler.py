##======================================================================================================================
#
def print_exception_warning(e: Exception, message: str = None, fp: str = None):
    """! @brief Standard method of outputting caught exceptions."""

    # Create the output string
    output_str = "START EXCEPTION\n" + f"EXCEPTION: {e}\n"

    # If a message was included
    if message != None:
        output_str += f"!!!GENERAL WARNING!!! {message}\n"

    # If a file path was included
    if fp != None:
        output_str += f"!!!FILE WARNING!!! IMPROPERLY FORMATTED FILE, REMOVING FROM THE LIST: {fp}\n"

    # Add ending string
    output_str += "END EXCEPTION\n"

    # Print the warning
    print(output_str)

    return
