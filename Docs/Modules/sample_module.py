# import packages

class module_name():
    name = str() # Name of Program
    desc = str() # Program description
    author = str() # John  Doe
    version = str() # 1.2.3
    mod_standard = str() # 1.0
    listeners = ['timer', 'voice']
    clock_req = False # Does it need access to Scheduler
    clock_jobs = [] 

    def __init__():
        """
        This function should be avoided for most tasks and start() should be used instead
        """
        # Add additional 
        # global x, y
        # x = 4
        # y = 1
        pass

    def scheduler_com():
        """
        This is what will be used to handle any Scheduler communication
        """
        pass

    def install():
        """
        Any post install tasks will be placed here
        """
        pass



    def start():
        """
        This is where your class is started when activated. Try to keep any required functions nested in this function. 
        """
        pass

    def end():
        """
        This is where you would prep disabling the application
        """
        pass

    def instanced():
        """
        This is what is going to run when an event is triggered based on the input
        """
        pass


