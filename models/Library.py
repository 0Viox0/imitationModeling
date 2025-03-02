from collections import deque
from models.Librarian import Librarian
from DistributionSampler import DistributionSampler

class Library:
    def __init__(self, num_books, copies_per_book, num_librarians, generator, normal_mean_librarian=2, normal_std_librarian=0.5):
        self.books = {f"Book_{i}": copies_per_book for i in range(num_books)}
        self.queues = {f"Book_{i}": deque() for i in range(num_books)}
        self.librarians = [Librarian(generator, normal_mean_librarian, normal_std_librarian) for _ in range(num_librarians)]
        self.wait_times = []
        self.served_users = 0
    
    def request_book(self, user, book_name, current_time):
        librarian = min(self.librarians, key=lambda x: x.available_at)
        librarian_time = librarian.serve_user(current_time)
        current_time = max(current_time, librarian_time)

        if self.books[book_name] > 0:
            self.books[book_name] -= 1
            self.wait_times.append(0)
            self.served_users += 1
            #print(f"{current_time:.2f}: User {user.user_id} took {book_name}")
            return (current_time, True)
        else:
            self.queues[book_name].append((user, current_time))
            #print(f"{current_time:.2f}: User {user.user_id} is waiting for {book_name}")
            return (current_time, False)
    
    def return_book(self, user, book_name, current_time):
        librarian = min(self.librarians, key=lambda x: x.available_at)
        librarian_time = librarian.serve_user(current_time)
        current_time = max(current_time, librarian_time)

        if self.queues[book_name]:
            next_user, request_time = self.queues[book_name].popleft()
            wait_time = current_time - request_time
            self.wait_times.append(wait_time)
            self.served_users += 1
            #print(f"{current_time:.2f}: User {user.user_id} returned {book_name}, now given to User {next_user.user_id}")
            return (current_time, next_user)
        else:
            self.books[book_name] += 1
            #print(f"{current_time:.2f}: User {user.user_id} returned {book_name}, now available")
            return (current_time, None)