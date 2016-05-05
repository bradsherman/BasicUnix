all: hello-dynamic hello-static hello-debug hello-profile

hello-dynamic: hello.c
	gcc -o hello-dynamic hello.c
hello-static: hello.c
	gcc -o hello-static hello.c -static
hello-debug: hello.c
	gcc -o hello-debug hello.c -g
hello-profile: hello.c
	gcc -o hello-profile hello.c -pg
clean:
	rm hello-*
