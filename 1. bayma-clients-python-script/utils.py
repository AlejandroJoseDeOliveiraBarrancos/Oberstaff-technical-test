import re
from datetime import datetime, timedelta
from config import MESSAGES, COLUMN_WIDTHS, TABLE_WIDTH, MENU_WIDTH


def validate_email(email):
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_name(name):
    return name and name.strip() and len(name.strip()) <= 100


def format_table_header():
    header = f"{'ID':<{COLUMN_WIDTHS['ID']}} "
    header += f"{'Name':<{COLUMN_WIDTHS['Name']}} "
    header += f"{'Email':<{COLUMN_WIDTHS['Email']}} "
    header += f"{'Discharged Date':<{COLUMN_WIDTHS['Discharged Date']}} "
    header += f"{'Active':<{COLUMN_WIDTHS['Active']}}"
    return header


def format_client_row(client_data):
    id, name, email, discharged_date, active = client_data
    active_status = "Yes" if active else "No"
    
    if isinstance(discharged_date, datetime):
        formatted_date = discharged_date.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(discharged_date, str):      
        try:
            parsed_date = datetime.fromisoformat(discharged_date.replace('Z', '+00:00'))
            formatted_date = parsed_date.strftime('%Y-%m-%d %H:%M:%S')
        except:
            formatted_date = discharged_date
    else:
        formatted_date = str(discharged_date)
    
    row = f"{id:<{COLUMN_WIDTHS['ID']}} "
    row += f"{name:<{COLUMN_WIDTHS['Name']}} "
    row += f"{email:<{COLUMN_WIDTHS['Email']}} "
    row += f"{formatted_date:<{COLUMN_WIDTHS['Discharged Date']}} "
    row += f"{active_status:<{COLUMN_WIDTHS['Active']}}"
    return row


def print_separator(width=MENU_WIDTH, char="="):
    print(char * width)


def print_menu_header(title):
    print_separator()
    print(title)
    print_separator()


def get_user_input(prompt, validator=None, error_message=None):
    while True:
        user_input = input(prompt).strip()
        
        if validator is None:
            return user_input
        
        if validator(user_input):
            return user_input
        else:
            print(error_message or "Invalid input. Please try again.")


def format_date(date_obj):
    if isinstance(date_obj, str):
        return date_obj
    
    if hasattr(date_obj, 'strftime'):
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')
    
    return str(date_obj)


def calculate_days_ago(days):
    return datetime.now().date() - timedelta(days=days)


def get_current_timestamp():
    return datetime.now() 