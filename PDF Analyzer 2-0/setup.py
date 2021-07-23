from cx_Freeze import Executable,setup

setup(
    name = "prueba1",
    executables = [Executable("main.py")]
)