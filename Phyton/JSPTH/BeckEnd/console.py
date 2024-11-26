import os
import argparse


class Console():
    def create_app(self, app_name):
        """Create a new app with a basic folder structure."""
        app_path = os.path.join(self.apps_dir, app_name)
        os.makedirs(os.path.join(app_path, 'templates'), exist_ok=True)
        os.makedirs(os.path.join(app_path, 'static/css'), exist_ok=True)
        os.makedirs(os.path.join(app_path, 'static/js'), exist_ok=True)
        
        # Create empty files
        with open(os.path.join(app_path, '__init__.py'), 'w') as f:
            f.write(f"# {app_name} app initialization")
        with open(os.path.join(app_path, 'routes.py'), 'w') as f:
            f.write(f"""# routes.py for {app_name} app


""")
        print(f"App '{app_name}' created successfully with necessary structure.")

    def register_apps(self):
        """Automatically load routes from each app's routes.py."""
        for app_name in os.listdir(self.apps_dir):
            app_path = os.path.join(self.apps_dir, app_name)
            routes_file = os.path.join(app_path, 'routes.py')
            if os.path.isdir(app_path) and os.path.exists(routes_file):
                # Dynamically import the routes module
                module_name = f"{self.apps_dir}.{app_name}.routes"
                __import__(module_name)
                print(f"Loaded routes for app '{app_name}'")

    def manage(self):
        """CLI to handle server commands and app creation."""
        parser = argparse.ArgumentParser(description="Manage your web application")
        subparsers = parser.add_subparsers(dest="command")

        # runserver command
        subparsers.add_parser("runserver", help="Start the development server")

        # createapp command
        createapp_parser = subparsers.add_parser("createapp", help="Create a new app")
        createapp_parser.add_argument("name", help="Name of the new app")

        # Parse command-line arguments
        args = parser.parse_args()

        # Execute commands based on args
        if args.command == "runserver":
            self.register_apps()
            self.run()
        elif args.command == "createapp":
            self.create_app(args.name)
        else:
            parser.print_help()