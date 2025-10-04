import sys
import logging

# when error raises we call this
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # exc_tb has all info of exception and exc_info has this param
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
         # Call the parent (Exception) constructor to initialize base error
        super().__init__(error_message) # since we are inheariting
         # Build a detailed message with filename, line number, and error
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
         # Return the detailed message whenever printed
        return self.error_message
    


    
        



