import sys

class PipelineGenerator():
    """Generate a valid python file to process user's dataset"""
    def __init__(modules=[]):
        self.lines = []
        for module in modules:
            self.lines+= "import " + module
        self.lines += ""

    def AddSteps(self, steps):
        """Add a new step to the pipeline"""
        for func in steps:
            self.lines += function

    def CreateLauncher(self, name):
        """Create a batch file to execute the script"""
        with open(name + "_launcher.bat", "w") as f:
            f.write("ECHO OFF")
            f.write("SET PATH=%PATH%;C:\Python"+ str(sys.version_info[0]) + str(sys.version_info[1]))
            f.write("python "+ name + ".py")
            f.write("PAUSE")

    def CreatePipeline(self, name):
        """Generate the pipeline script for processing the data"""
        with open(name + ".py", "w") as f:
            for line in self.lines:
                f.write(line)

