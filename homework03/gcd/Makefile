CC=		gcc
CFLAGS=		-o
LD=		gcc
LDFLAGS=	-shared
AR=		ar
ARFLAGS=	-ru
TARGETS=	libgcd.a libgcd.so gcd-static gcd-dynamic

all:	$(TARGETS)

gcd-static: main.o libgcd.a
	$(CC) -static $^ $(CFLAGS) $@ 

gcd-dynamic: main.o libgcd.so
	$(CC) $^ $(CFLAGS) $@ 

libgcd.a: gcd.o
	$(AR) $(ARFLAGS) $@ $<

libgcd.so: gcd.o
	$(LD) $(LDFLAGS) $< $(CFLAGS) $@

%.o: %.c
	$(CC) -c $< $(CFLAGS) $@

clean:
	rm -f $(TARGETS) *.o
