###Cinema Ticket Pre-Sale Application

def get_ticket_request(remaining_tickets: int) -> int:
    """
  Brief description:
        Prompt the user for the number of tickets they want to buy and validate the request.

    Parameters:
        remaining_tickets (int)

    Variables:
        request_str (str)
        requested_tickets (int):

Check if tickets are available, if yes return tickets, if no say none left

    Return:
        purchased ticket qty (int)
    """
    while True:
        # Prompt the user for the number of tickets they want to buy.
        request_str = input("Pray tell, how many tickets wouldst thou claim, O moviegoer supreme (1-4)? ")

        # Validate that the input is numeric before converting.
        if not request_str.strip().isdigit():
            # Explain why the input is rejected so the user can correct it.
            print("Invalid entry. Please enter a whole number from 1 to 4.")
            print()
            continue

        # Convert the validated numeric string into an integer.
        requested_tickets = int(request_str)

        # Enforce the per-buyer maximum and minimum purchase rule.
        if requested_tickets < 1 or requested_tickets > 4:
            # Inform the user about the allowed range.
            print("Invalid number of tickets. You may purchase 1 to 4 tickets per buyer.")
            print()
            continue

        # Prevent selling more tickets than remain.
        if requested_tickets > remaining_tickets:
            # Explain that the request exceeds the remaining inventory.
            print(f"Only {remaining_tickets} ticket(s) remain. Please enter a smaller number.")
            print()
            continue

        # Return the validated request.
        return requested_tickets


def run_ticket_presale(ticket_stockpile: int = 10) -> None:
    """
  Brief description:
    Runs the ticket pre-sale process until all tickets are sold and displays the total number of buyers.

Parameters:
    ticket_stockpile (int): The total number of tickets available.

Variables:
    remaining_tickets (int): Tracks how many tickets are left.
    buyer_count (int): Counts how many buyers purchased tickets.

    Return:
        None
    """
    # Store the remaining tickets so we can update the count after each purchase.
    remaining_tickets = ticket_stockpile

    # Accumulate the number of buyers who successfully purchased tickets.
    buyer_count = 0

    # Provide a friendly start message so the user understands the constraints.
    print("Welcome to the Cinema Ticket Pre-Sale!")
    print("Each buyer may purchase up to 4 tickets.")
    print(f"There are {ticket_stockpile} tickets available in total.")
    print()

    # Continue selling tickets until none remain.
    while remaining_tickets > 0:
        # Get a valid request that respects both the per-buyer limit and remaining tickets.
        requested_tickets = get_ticket_request(remaining_tickets)

        # Reduce the remaining tickets based on the buyer's purchase.
        remaining_tickets -= requested_tickets

        # Count this buyer using an accumulator.
        buyer_count += 1

        # Display the remaining tickets after the purchase.
        print(f"Purchase complete. Tickets remaining: {remaining_tickets}")
        print()

        # If tickets are sold out, end the sale with a clear message.
        if remaining_tickets == 0:
            # Inform the user that no additional purchases can occur.
            print("Sold out! No tickets remain.")
            print(f"Total number of buyers: {buyer_count}")


if __name__ == "__main__":
    # Run the application with the default ticket inventory of 20.
    run_ticket_presale()
