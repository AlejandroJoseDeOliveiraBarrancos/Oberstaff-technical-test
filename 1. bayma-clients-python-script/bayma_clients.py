#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import sys

from config import DB_CONFIG, MESSAGES, MENU_OPTIONS, APP_NAME
from queries import ClientQueries
from utils import (
    validate_email, validate_name, format_table_header, format_client_row,
    print_separator, print_menu_header, get_user_input, calculate_days_ago, get_current_timestamp
)


class BaymaClientsManager:
    def __init__(self, db_config=None):
        if db_config is None:
            db_config = DB_CONFIG
            
        self.host = db_config['host']
        self.user = db_config['user']
        self.password = db_config['password']
        self.database = db_config['database']
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print(MESSAGES['connection_success'])
                return True
        except Error as e:
            print(MESSAGES['connection_error'].format(e))
            return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print(MESSAGES['connection_closed'])

    def list_active_clients_last_60_days(self):
        try:
            cursor = self.connection.cursor()
            
            sixty_days_ago = calculate_days_ago(60)
            
            cursor.execute(ClientQueries.LIST_ACTIVE_CLIENTS_60_DAYS, (sixty_days_ago,))
            results = cursor.fetchall()
            
            if results:
                print(f"\n{MESSAGES['clients_found']}")
                print("-" * 100)
                print(format_table_header())
                print("-" * 100)
                
                for row in results:
                    print(format_client_row(row))
                
                print(f"\n{MESSAGES['total_clients'].format(len(results))}")
            else:
                print(f"\n{MESSAGES['no_clients_found']}")
                
        except Error as e:
            print(MESSAGES['error_listing'].format(e))
        finally:
            if cursor:
                cursor.close()

    def add_new_client(self):
        try:
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
            
            cursor = self.connection.cursor()
            
            cursor.execute(ClientQueries.CHECK_EMAIL_EXISTS, (email,))
            if cursor.fetchone():
                print(MESSAGES['email_exists'])
                return
            
            current_timestamp = get_current_timestamp()
            cursor.execute(ClientQueries.INSERT_NEW_CLIENT, (name, email, current_timestamp))
            self.connection.commit()
            
            print(MESSAGES['client_added'].format(name))
            print(f"   Email: {email}")
            print(f"   Discharged Date: {current_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            
        except Error as e:
            print(MESSAGES['error_adding'].format(e))
        finally:
            if cursor:
                cursor.close()

    def deactivate_client(self):
        try:
            print(f"\n{MESSAGES['deactivating_client']}")
            
            email = get_user_input(
                "Enter client email to deactivate: ",
                validator=lambda x: x and x.strip(),
                error_message=MESSAGES['email_empty']
            )
            if not email:
                return
            
            cursor = self.connection.cursor()
            
            cursor.execute(ClientQueries.GET_CLIENT_BY_EMAIL, (email,))
            result = cursor.fetchone()
            
            if not result:
                print(MESSAGES['client_not_found'])
                return
            
            client_id, client_name, is_active = result
            
            if not is_active:
                print(MESSAGES['client_already_deactivated'].format(client_name))
                return
            
            cursor.execute(ClientQueries.DEACTIVATE_CLIENT, (email,))
            self.connection.commit()
            
            print(MESSAGES['client_deactivated'].format(client_name, client_id))
            
        except Error as e:
            print(MESSAGES['error_deactivating'].format(e))
        finally:
            if cursor:
                cursor.close()

    def show_menu(self):
        print_menu_header(APP_NAME)
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
    print(MESSAGES['app_start'])
    
    manager = BaymaClientsManager()
    manager.run()


if __name__ == "__main__":
    main() 