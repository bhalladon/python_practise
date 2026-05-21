class Variable:
    """
    This is a class that shows local and global variables
    """
    global_var = "I am global"

    def print_string(self):
        local_var = "I am local"
        new_var = self.global_var + local_var
        print(new_var)

    print(global_var)


a = Variable()
a.print_string()
