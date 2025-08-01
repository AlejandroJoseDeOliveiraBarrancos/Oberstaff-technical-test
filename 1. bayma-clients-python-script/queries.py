class ClientQueries:
    LIST_ACTIVE_CLIENTS_60_DAYS = """
        SELECT id, name, email, discharged_date, active 
        FROM clientes 
        WHERE active = 1 AND discharged_date >= %s 
        ORDER BY discharged_date DESC
    """
    
    CHECK_EMAIL_EXISTS = """
        SELECT id FROM clientes WHERE email = %s
    """
    
    INSERT_NEW_CLIENT = """
        INSERT INTO clientes (name, email, discharged_date, active) 
        VALUES (%s, %s, %s, 1)
    """
    
    GET_CLIENT_BY_EMAIL = """
        SELECT id, name, active FROM clientes WHERE email = %s
    """
    
    DEACTIVATE_CLIENT = """
        UPDATE clientes SET active = 0 WHERE email = %s
    """
    
    GET_ALL_CLIENTS = """
        SELECT id, name, email, discharged_date, active 
        FROM clientes 
        ORDER BY discharged_date DESC
    """
    
    GET_CLIENT_COUNT = """
        SELECT COUNT(*) FROM clientes
    """
    
    GET_ACTIVE_CLIENT_COUNT = """
        SELECT COUNT(*) FROM clientes WHERE active = 1
    """ 