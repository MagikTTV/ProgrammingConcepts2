import sqlite3
import random
import matplotlib.pyplot as plt


DATABASE_NAME = "population_JA.db"


def create_database():
    """
    Creates the population database and population table.
    """

    # Connect to the SQLite database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a cursor to run SQL commands.
    cursor = connection.cursor()

    # Create the population table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Clear old data so the program does not duplicate records.
    cursor.execute("DELETE FROM population")

    # Save changes and close the database.
    connection.commit()
    connection.close()


def insert_2025_population():
    """
    Inserts 2025 population data for 10 Florida cities.
    """

    # List of Florida cities and sample 2025 population data.
    city_data = [
        ("Jacksonville", 1000000),
        ("Miami", 455000),
        ("Tampa", 410000),
        ("Orlando", 325000),
        ("St. Petersburg", 265000),
        ("Hialeah", 225000),
        ("Tallahassee", 205000),
        ("Port St. Lucie", 245000),
        ("Cape Coral", 230000),
        ("Fort Lauderdale", 185000)
    ]

    # Connect to the database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a cursor to run SQL commands.
    cursor = connection.cursor()

    # Insert each city into the table.
    cursor.executemany("""
        INSERT INTO population (city, year, population)
        VALUES (?, ?, ?)
    """, [(city, 2025, population) for city, population in city_data])

    # Save changes and close the database.
    connection.commit()
    connection.close()


def simulate_population_change():
    """
    Simulates population growth and decline for the next 20 years.
    """

    # Connect to the database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a cursor to run SQL commands.
    cursor = connection.cursor()

    # Get the original 2025 population records.
    cursor.execute("""
        SELECT city, population
        FROM population
        WHERE year = 2025
    """)

    # Store the 2025 city data.
    city_data = cursor.fetchall()

    # Loop through each city.
    for city, starting_population in city_data:

        # Set the current population.
        current_population = starting_population

        # Create population records from 2026 through 2045.
        for year in range(2026, 2046):

            # Choose a random growth or decline rate between -2% and 3%.
            rate = random.uniform(-0.02, 0.03)

            # Calculate the new population.
            current_population = int(current_population * (1 + rate))

            # Insert the simulated population into the database.
            cursor.execute("""
                INSERT INTO population (city, year, population)
                VALUES (?, ?, ?)
            """, (city, year, current_population))

    # Save changes and close the database.
    connection.commit()
    connection.close()


def display_city_options():
    """
    Displays the city options for the user.
    """

    # Connect to the database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a cursor to run SQL commands.
    cursor = connection.cursor()

    # Get the city names.
    cursor.execute("""
        SELECT DISTINCT city
        FROM population
        ORDER BY city
    """)

    # Store the cities.
    cities = [row[0] for row in cursor.fetchall()]

    # Close the database.
    connection.close()

    # Print the city options.
    print("\nFlorida city options:")

    for number, city in enumerate(cities, start=1):
        print(f"{number}. {city}")

    return cities


def graph_population_for_city(city):
    """
    Creates a line graph showing population growth or decline for one city.

    Parameters:
        city (str): The city selected by the user.
    """

    # Connect to the database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a cursor to run SQL commands.
    cursor = connection.cursor()

    # Get the population data for the selected city.
    cursor.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (city,))

    # Store the results.
    records = cursor.fetchall()

    # Close the database.
    connection.close()

    # Separate years and populations into lists.
    years = [record[0] for record in records]
    populations = [record[1] for record in records]

    # Create the line graph.
    plt.plot(years, populations, marker="o")

    # Add the graph title and labels.
    plt.title(f"Population Growth and Decline for {city}")
    plt.xlabel("Year")
    plt.ylabel("Population")

    # Add a grid for readability.
    plt.grid(True)

    # Display the graph.
    plt.show()


def main():
    """
    Runs the population database program.
    """

    # Create the database and table.
    create_database()

    # Insert starting 2025 population data.
    insert_2025_population()

    # Simulate population changes for 20 years.
    simulate_population_change()

    # Display city choices.
    cities = display_city_options()

    # Ask the user to select a city.
    choice = int(input("\nChoose a city by entering its number: "))

    # Validate the user's choice.
    if 1 <= choice <= len(cities):
        selected_city = cities[choice - 1]
        graph_population_for_city(selected_city)
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()