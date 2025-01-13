def read_all(connection):
    conn = connection
    cursor = conn.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)

    resultat = cursor.fetchall()
    cursor.close()

    return resultat