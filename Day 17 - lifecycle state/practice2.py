
def prob1():
    """invariant - the pool can hold 2 active users, invalid requests are rejected or dropped"""

    stream = [
        ("CONNECT", "Alice"),
        ("CONNECT", "Bob"),
        ("CONNECT", "Alice"), # Idempotent (already connected) -> Silent drop
        ("CONNECT", "Charlie"), # Pool full (Alice, Bob) -> REJECT
        ("DISCONNECT", "Alice"), # Alice leaves. Pool: (Bob)
        ("DISCONNECT", "Dave"),  # Ghost disconnect -> Silent drop
        ("CONNECT", "Charlie")   # Pool has space. -> Accept
    ]

    pool = {}

    for action, user_id in stream:
        
        if user_id in pool and action == "DISCONNECT":
            pool.pop(user_id)

        elif user_id not in pool and action == "CONNECT":
            if len(pool) < 2:
                pool[user_id] = action
            else:
                print(f"can't accept {user_id}. Max limit reached")

        print(pool)

prob1()


"""the connnect for every user is useless memory waste. if the user is in pool, that means that user
    is connected -- just storing user id will also work using set()"""