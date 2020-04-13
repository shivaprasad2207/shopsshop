use File::Slurp qw/read_file/;
print CGI::header();
my $html =read_file('xx.html');
print $html;