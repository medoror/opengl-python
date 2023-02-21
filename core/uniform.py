from OpenGL.GL import *
import numpy


class Attribute(object):
    def __init__(self, dataType, data):
        # type fo elements in data array:
        # int | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # array of data to be stored in buffer
        self.data = data

        # reference for variable location in the program
        self.variableRef = None

    # get and store reference for program with given name
    def associateVariable(self, programRef, variableName):
        # get reference for program variable given name
        variableRef = glGetUniformLocation(programRef, variableName)

        def uploadData(self):
            if variableRef == -1:
                return
            if self.dataType == "int":
                glUniform1i(variableRef, self.data)
            elif self.dataType == "bool":
                glUniform1i(variableRef, self.data)
            elif self.dataType == "float":
                glUniform1f(variableRef, self.data)
            elif self.dataType == "vec2":
                glUniform2f(variableRef, self.data[0], self.data[1])
            elif self.dataType == "vec3":
                glUniform3f(variableRef, self.data[0], self.data[1], self.data[2])
            elif self.dataType == "vec4":
                glUniform4f(variableRef, self.data[0], self.data[1], self.data[2], self.data[3])
            else:
                raise Exception("Uniform val " + variableName + " has unknown type " + self.dataType)
