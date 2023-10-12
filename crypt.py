import marshal
import os

while True:
    my_file_path = input("Write path file (or 'exit' to quit): ").strip('"')

    if my_file_path.lower() == 'exit':
        break

    try:
        with open(my_file_path, 'r') as file:
            file_content = file.read()
            compile_file = compile(file_content, '', 'exec')
            encrypt = marshal.dumps(compile_file)

        file_name = os.path.basename(my_file_path)
        new_file_path = 'New_' + file_name
        with open(new_file_path, 'w') as code:
            code.write("import marshal\n")
            code.write('exec(marshal.loads(' + repr(encrypt) + '))')

        print("The file encrypted: " + new_file_path)
        break
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))
