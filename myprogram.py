#__init__.py in a folder declares the folder as a package
#And the .py scripts inside it are its modules which can be imported like shown below
from MyMainPackage import mymainscript #This is how you import the script from a package
from MyMainPackage.MySubPackage import mysubscript #This is how you import a subscript from a subscript package using (.)

mymainscript.mainscript_func() #calling a function of the mainscript module
mysubscript.subscript_func() #calling a function of the subscript module