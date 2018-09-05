import os, time
def pertama():
    print """\033[1;33m\n
install beberapa keperluan:
    $ pkg install -y perl make
    $ pkg install git
    $ pkg install wget
    $ pkg install tar\n\n """
    jut = "ketik \"enter\" untuk lanjut"
    kedua()
def kedua():
    print """\033[1;34m\n
lanjut:
    $ wget http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/HTTP-Message-6.14.tar.gz
    $ tar zxf HTTP-Message-6.14.tar.gz
    $ cd HTTP-Message-6.14
    $ perl Makefile.PL
    $ make
    $ make test
    $ make install\n\n """
    jut = "ketik \"enter\" untuk lanjut"
    ketiga()
def ketiga():
    print """\033[1;35m\n
masih di directory HTTP-Message-6.14:
    $ wget http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/libwww-perl-6.31.tar.gz
    $ tar zxf libwww-perl-6.31.tar.gz
    $ cd libwww-perl-6.31
    $ perl Makefile.PL
    $ make
    $ make test
    $ make install\n\n"""
    jut = "ketik \"enter\" untuk lanjut"
    keempat()
def keempat():
    print """\033[1;36m\n
terakhir:
    $ cpan install Getopt::Long
    $ cpan install HTTP::Request
    $ cpan install LWP::UserAgent
    $ cpan install IO::Select
    $ cpan install HTTP::Cookies
    $ cpan install HTTP::Response
    $ cpan install Term::ANSIColor
    $ cpan install URI::URL
    $ cpan install IO::Socket::INET
    $ cpan install Try::Tiny\n\n"""
    jut = "ketik \"enter\" untuk lanjut"
    print "semua selesai ^_^"
    time.sleep(0.4)
    print "kembali ke $HOME\ndengan mengetik cd $HOME"
    time.sleep(0.5)
    print "kalian masuk ke directory XAttacker"
    time.sleep(0.3)
    print "dan selamat menikmati"
print "\033[1;31mXAttacker \033[1;32minstaller"
print "\033[1;33m1. install step by step\n\033[1;34m2. install auto"
apa = input("\033[1;32mpilih ")
if apa == 1:
    pertama()
elif apa == 2:
    time.sleep(0.6)
    print """\033[1;35m
1. pastikan XAttacker belum diinstall
2. selalu onlen
3. sedia kopi bila perlu v:"""
    nanya = raw_input("lanjut?\n[Y/N] ")
    if nanya == "Y" or nanya == "y":
        print "please wait..."
        time.sleep(0.3)
        os.system("sh install.sh")
    elif nanya == "N" or nanya == "n":
        exit("\033[1;31mwokek")
