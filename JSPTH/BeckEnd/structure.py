import os

def create_project_structure(project_name):
    # Define the directory structure
    structure = {
        project_name: [
            'app/',
            'app/templates/',
            'app/static/',
            'app/static/css/',
            'app/static/js/',
            'app/static/images/',
        ],
        f'{project_name}/app': [
            '__init__.py',
            'routes.py'
        ],
        f'{project_name}/app/templates': [
            'index.html',
            'hello.html'
        ],
        f'{project_name}/app/static/css': [
            'style.css'
        ],
        f'{project_name}/app/static/js': [
            'script.js'
        ],
        project_name: [
            'simple_server.py',
            'config.py',
            'main.py',
            'README.md'
        ]
    }

    # Create directories and files based on the structure
    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    if file == 'README.md':
                        f.write(f"# {project_name.capitalize()}\n\nProject documentation.")
                    elif file.endswith('.html'):
                        f.write("<-- Write your html-->")
                    elif file.endswith('.css'):
                        f.write("/* Add your CSS here */")
                    elif file.endswith('.js'):
                        f.write("// Add your JavaScript here")
                    elif file == 'routes.py':
                        f.write("# Define your route functions here\n\n")
                    elif file == 'main.py':
                        f.write(f"""# main.py

from JSPTH.BeckEnd.server import SimpleServer
from app_routes import routes  # Import your routes

app = SimpleServer(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    app.run()
""")
                    elif file == 'config.py':
                        f.write("# Configuration settings for your application\n")
                    else:
                        f.write("")

    print(f"Project '{project_name}' created successfully!")

if __name__ == '__main__':
    project_name = input("Enter the project name: ")
    create_project_structure(project_name)
