from datetime import datetime

with open("deployed_at.txt", "w") as f:
    f.write(f"Last deployed at: {datetime.now()}")

print("Deployment marker updated")
