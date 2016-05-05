CC=		gcc
CFLAGS=		-g -o
TARGETS=	is_palindrome

all:	$(TARGETS)

is_palindrome: is_palindrome.c
	$(CC) is_palindrome.c $(CFLAGS) is_palindrome

clean:
	rm -f $(TARGETS) *.o

test: is_palindrome is_palindrome.input is_palindrome.output
	./is_palindrome < is_palindrome.input > is_palindrome.output2
	diff is_palindrome.output2 is_palindrome.output
