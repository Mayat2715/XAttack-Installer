#!/data/data/com.termux/files/usr/bin/bash
pkg install -y perl make git wget tar
cd $HOME
git clone https://github.com/Moham3dRiahi/XAttacker
cd XAttacker
echo "menginstall HTTP-Message-6.14 dan libwww-perl-6.31"
sleep 1.2
wget http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/HTTP-Message-6.14.tar.gz
tar zxf HTTP-Message-6.14.tar.gz
cd HTTP-Message-6.14
perl Makefile.PL
make
make test
make install
wget http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/libwww-perl-6.31.tar.gz
tar zxf libwww-perl-6.31.tar.gz
cd libwww-perl-6.31
perl Makefile.PL
make
make test
make install
cpan install Getopt::Long
cpan install HTTP::Request
cpan install LWP::UserAgent
cpan install IO::Select
cpan install HTTP::Cookies
cpan install HTTP::Response
cpan install Term::ANSIColor
cpan install URI::URL
cpan install IO::Socket::INET
cpan install Try::Tiny
cd $HOME
sleep 1
echo "\033[33;1msemua selesai"
sleep 0.7
echo "\033[32;1mhave fun^_^"
