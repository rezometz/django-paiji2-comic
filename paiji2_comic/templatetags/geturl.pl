#!/usr/bin/env perl
# geturl.pl
# should return an url
use strict;
use warnings;
use WWW::Mechanize;

# settings
my $mech = WWW::Mechanize->new(
	# noproxy => 1,
	autocheck => 1,
);
$mech->agent_alias('Windows Mozilla');
my $baseurl = 'http://www.gocomics.com/';

my $comic = $ARGV[0];
my $url = "$baseurl$comic";
$mech->get($url) || exit 1;
my @strips = $mech->find_all_images(
	url_regex => qr/assets\.amuniversal\.com/,
) || exit 2;
my $strip = $strips[1] || exit 3;;  # second img (better quality)
print $strip->url();
exit 0;
