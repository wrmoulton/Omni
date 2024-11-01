import omni.ext
import omni.ui as ui
from omni.kit.window.filepicker import FilePickerDialog
import csv

class ViewerCsvfileExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[viewer.csvfile] company hello world startup")

        # String model for file path display
        self.uiModel = ui.SimpleStringModel("Select A File")

        # Main window setup
        self._window = ui.Window("CSV Viewer", width=500, height=400)
        with self._window.frame:
            with ui.VStack(spacing=5):  # Reduced spacing for compactness
                # File selection label and display
                with ui.HStack(height=30,spacing=5):
                    ui.Label("Selected File:", style={"color": 0xAAAAAAFF, "font_size": 14})
                    self.file_path_display = ui.StringField(model=self.uiModel, enabled=False, height=0, width=380)  # Adjusted width

                # Browse button for file selection
                ui.Button("Browse", clicked_fn=self.open_file_picker, height=30)  # Compact height

                # Collapsible section for CSV content
                with ui.CollapsableFrame("CSV Data", collapsed=True):  # Collapsed by default
                    self.csv_content_area = ui.ScrollingFrame(height=250)

    def open_file_picker(self):
        # Restricting file selection to CSV files
        self.filepicker = FilePickerDialog(
            title="Select a CSV File",
            apply_button_label="Open",
            click_apply_handler=self.on_file_selected,
            click_cancel_handler=self.on_cancel_selection,  # Cancel handler added here
            file_extensions=["csv"],
            width=800,
            height=400
        )
        self.filepicker.show()

    def on_file_selected(self, file_name, dir_name):
        # Callback when a CSV file is selected
        file_path = f"{dir_name}/{file_name}"
        self.uiModel.as_string = file_path  # Update the StringField's model
        print(f"[viewer.csvfile] File selected: {file_path}")
        
        # Close the file picker dialog
        if self.filepicker:
            self.filepicker.hide()

        # Display the CSV content
        self.display_csv_content(file_path)

    def on_cancel_selection(self, file_name, dir_name):
        # Callback when the Cancel button is clicked
        print("[viewer.csvfile] File selection was canceled.")
        if self.filepicker:
            self.filepicker.hide()  # Close the file picker dialog

    def display_csv_content(self, file_path):
        try:
            # Clear previous content
            self.csv_content_area.clear()
            
            # Create a vertical stack to hold CSV rows
            with self.csv_content_area:
                with ui.VStack(spacing=5):
                    # Read the CSV file and display rows
                    with open(file_path, 'r') as file:
                        reader = csv.reader(file)
                        headers = next(reader, None)  # Get headers
                        
                        # Display headers
                        if headers:
                            ui.Label(", ".join(headers), style={"font_size": 12, "color": 0xFFFFFF80})
                        
                        # Display rows of data
                        for row in reader:
                            ui.Label(", ".join(row), style={"font_size": 12, "color": 0xFFFFFFB0})

        except Exception as e:
            print(f"[viewer.csvfile] Error reading CSV file: {e}")
            ui.Label("Error reading file", style={"color": 0xFF0000FF})

    def on_shutdown(self):
        print("[viewer.csvfile] company hello world shutdown")

