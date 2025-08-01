DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'clientes_bayma'
}

APP_NAME = "Bayma Clients Management System"
APP_VERSION = "1.0.0"

MENU_OPTIONS = {
    '1': 'List active clients (last 60 days)',
    '2': 'Add new client',
    '3': 'Deactivate client',
    '4': 'Exit'
}

TABLE_WIDTH = 100
MENU_WIDTH = 50
COLUMN_WIDTHS = {
    'ID': 5,
    'Name': 25,
    'Email': 30,
    'Discharged Date': 20,
    'Active': 8
}

MESSAGES = {
    'connection_success': "Successfully connected to MySQL database!",
    'connection_error': "Error connecting to MySQL: {}",
    'connection_closed': "Database connection closed.",
    'connection_failed': "Failed to connect to database. Please check your connection parameters.",
    'app_start': "Starting Bayma Clients Management System...",
    'app_goodbye': "Goodbye!",
    'app_interrupted': "Application interrupted. Goodbye!",
    'invalid_option': "Invalid option. Please select 1-4.",
    'press_continue': "Press Enter to continue...",
    'no_clients_found': "No active clients found in the last 60 days.",
    'clients_found': "Active clients registered in the last 60 days:",
    'total_clients': "Total: {} active client(s)",
    'adding_client': "Adding new client...",
    'deactivating_client': "Deactivating client...",
    'name_empty': "Name cannot be empty!",
    'email_empty': "Email cannot be empty!",
    'invalid_email': "Invalid email format!",
    'email_exists': "A client with this email already exists!",
    'client_added': "Client '{}' added successfully!",
    'client_deactivated': "Client '{}' (ID: {}) deactivated successfully!",
    'client_not_found': "No client found with this email!",
    'client_already_deactivated': "Client '{}' is already deactivated!",
    'error_listing': "Error listing clients: {}",
    'error_adding': "Error adding client: {}",
    'error_deactivating': "Error deactivating client: {}"
} 