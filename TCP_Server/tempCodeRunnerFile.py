# Accept a connection
conn, addr = s.accept()

# Receive the bytes over the connection
data = conn.recv(1024)
