import os;

print(os.environ)
print(os.environ.get("HOME"))

print(os.listdir())
print(os.path.exists('modules'))
print(os.path.isdir('modules'))
print(os.path.isfile('os.py'))
print(os.path.islink('os.py'))

print(os.path.getsize('20_os_1_file_directory_struc.py'))
print(os.getgid())
print(os.getpid())
print(os.getuid())