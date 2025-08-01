#!/usr/bin/env python3
import sys
from datetime import datetime, timedelta

from config import MESSAGES, MENU_OPTIONS, APP_NAME
from utils import (
    validate_email, validate_name, format_table_header, format_client_row,
    print_separator, print_menu_header, get_user_input, calculate_days_ago, get_current_timestamp
)


class MockBaymaClientsManager:
    def __init__(self):
        self.mock_clients = [
            {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'discharged_date': '2024-01-15 14:30:25', 'active': True},
            {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@company.com', 'discharged_date': '2024-01-10 09:15:42', 'active': True},
            {'id': 3, 'name': 'Bob Johnson', 'email': 'bob.johnson@test.com', 'discharged_date': '2024-01-05 16:45:18', 'active': True},
            {'id': 4, 'name': 'Alice Brown', 'email': 'alice.brown@email.com', 'discharged_date': '2023-12-01 11:20:33', 'active': False},
        ]
    
    def connect(self):
        print(f"{MESSAGES['connection_success']} (MOCK)")
        return True
    
    def disconnect(self):
        print(f"{MESSAGES['connection_closed']} (MOCK)")
    
    def list_active_clients_last_60_days(self):
        print(f"\n{MESSAGES['clients_found']}")
        print("-" * 100)
        print(format_table_header())
        print("-" * 100)
        
        sixty_days_ago = calculate_days_ago(60)
        active_recent = [
            client for client in self.mock_clients 
            if client['active'] and datetime.strptime(client['discharged_date'], '%Y-%m-%d %H:%M:%S').date() >= sixty_days_ago
        ]
        
        active_recent.sort(key=lambda x: x['discharged_date'], reverse=True)
        
        for client in active_recent:
            client_data = (
                client['id'], 
                client['name'], 
                client['email'], 
                client['discharged_date'], 
                client['active']
            )
            print(format_client_row(client_data))
        
        print(f"\n{MESSAGES['total_clients'].format(len(active_recent))}")
    
    def add_new_client(self):
        print(f"\n{MESSAGES['adding_client']}")
        
        name = get_user_input(
            "Enter client name: ",
            validator=validate_name,
            error_message=MESSAGES['name_empty']
        )
        if not name:
            return
        
        email = get_user_input(
            "Enter client email: ",
            validator=validate_email,
            error_message=MESSAGES['invalid_email']
        )
        if not email:
            return
        
        if any(client['email'] == email for client in self.mock_clients):
            print(MESSAGES['email_exists'])
            return
        
        new_id = max(client['id'] for client in self.mock_clients) + 1
        current_timestamp = get_current_timestamp()
        current_date_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        new_client = {
            'id': new_id,
            'name': name,
            'email': email,
            'discharged_date': current_date_str,
            'active': True
        }
        
        self.mock_clients.append(new_client)
        
        print(MESSAGES['client_added'].format(name))
        print(f"   Email: {email}")
        print(f"   Discharged Date: {current_date_str}")
    
    def deactivate_client(self):
        print(f"\n{MESSAGES['deactivating_client']}")
        
        email = get_user_input(
            "Enter client email to deactivate: ",
            validator=lambda x: x and x.strip(),
            error_message=MESSAGES['email_empty']
        )
        if not email:
            return
        
        client = next((c for c in self.mock_clients if c['email'] == email), None)
        
        if not client:
            print(MESSAGES['client_not_found'])
            return
        
        if not client['active']:
            print(MESSAGES['client_already_deactivated'].format(client['name']))
            return
        
        client['active'] = False
        
        print(MESSAGES['client_deactivated'].format(client['name'], client['id']))
    
    def show_menu(self):
        print_menu_header(f"{APP_NAME} (MOCK)")
        for key, value in MENU_OPTIONS.items():
            print(f"{key}. {value}")
        print_separator()
    
    def run(self):
        if not self.connect():
            print(MESSAGES['connection_failed'])
            return
        
        try:
            while True:
                self.show_menu()
                choice = input("\nSelect an option (1-4): ").strip()
                
                if choice == '1':
                    self.list_active_clients_last_60_days()
                elif choice == '2':
                    self.add_new_client()
                elif choice == '3':
                    self.deactivate_client()
                elif choice == '4':
                    print(f"\n{MESSAGES['app_goodbye']}")
                    break
                else:
                    print(MESSAGES['invalid_option'])
                
                input(f"\n{MESSAGES['press_continue']}")
                
        except KeyboardInterrupt:
            print(f"\n\n{MESSAGES['app_interrupted']}")
        finally:
            self.disconnect()


def main():
    print(f"{MESSAGES['app_start']} (MOCK)")
    print("This is a demonstration version that simulates database operations.")
    
    manager = MockBaymaClientsManager()
    manager.run()


if __name__ == "__main__":
    main() 