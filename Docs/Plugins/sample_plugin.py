# import packages

class Plugin():
    name = str() # Name of Program
    desc = str() # Program description
    author = str() # John  Doe
    version = str() # 1.2.3
    mod_standard = str() # 1.0
    listeners = ['timer', 'voice']
    clock_req = False # Does it need access to Scheduler
    clock_jobs = [] 
    trigger_actions = []
    trigger_words = []

    def __init__(self, *args, **kwargs):
        """
        This function should be avoided for most tasks and start() should be used instead
        """
        # Add additional 
        # global x, y
        # x = 4
        # y = 1
        pass

    def scheduler_com(self):
        """
        This is what will be used to handle any Scheduler communication
        """
        pass

    def install(self):
        """
        Any post install tasks will be placed here
        """
        pass


    def start(self):
        """
        This is where your class is started when activated. Try to keep any required functions nested in this function. 
        """
        pass


    def instanced(self):
        """
        This is what is going to run when an event is triggered based on the input
        """
        pass

